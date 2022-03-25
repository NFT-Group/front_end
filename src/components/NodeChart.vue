<template>
    <form @submit="onSubmit">
      <label>Choose a Collection:</label>
        <select value="collection" id="collection" name="collection">
            <option value="cryptoPunks" id="punk" name="collection">CryptoPunks</option>
            <option value="boredApeYachtClub" id="boredape" name="collection" selected="selected">Bored Ape Yacht Club</option>
            <option value="boredapekennel" id="boredapekennel" name="collection">Bored Ape Kennel Club</option>
            <option value="doodle" id="doodle" name="collection">Doodles</option>
            <option value="coolcat" id="coolcat" name="collection">Cool Cats</option>
            <option value="cryptoad" id="cryptoad" name="collection">CrypToadz</option>
            <option value="penguin" id="penguin" name="collection">Pudgy Penguins</option>
            <option value="clonex" id="clonex" name="collection">cloneX</option>
        </select>
        <br><br>
        <input type="submit" name="submit_button">
    </form>
    <p> Hover for transaction destination/ origin. <br>
    Click on Wallet Names/ Wallet IDs to view OpenSea account. <br>
    Red link = Sale <br>
    Blue link = Purchase </p>
    <div id="charts">
        <svg id="nodeChart" width="1350" height="1000"></svg>
    </div>
</template>

<script>
    import * as d3 from 'd3';
    import data1 from '../../public/node_graph_data/boredApeYachtClub.json'
    import data2 from '../../public/node_graph_data/cryptoPunks.json'

    export default {
        mounted: function () {
            this.renderChart('boredApeYachtClub');
        },
        methods: {
            onSubmit(evt) {
                // Refresh SVG 
                var svg_reset = d3.select("#nodeChart")
	            svg_reset.selectAll("*").remove()
                evt.preventDefault();
                var collection = evt.srcElement.collection.value
                this.renderChart(collection)
            },
            renderChart(JSONname)
            {   
                var data;
                if(JSONname == 'boredApeYachtClub')
                {
                    data = data1;
                }
                if(JSONname == 'cryptoPunks')
                {
                    data = data2;
                }
                
                var diameter = 1000,
                innerCircle = 100,
                radius = diameter / 2 - innerCircle;

                var svg = d3.select("#nodeChart")
                    .attr("width", diameter)
                    .attr("height", diameter);

                var stratify = d3.stratify()
                    .id(d => d.name);

                var cluster = d3.cluster()
                    .size([Math.PI * 2, radius]);

                var line = d3.line()
                    .x(d => getX(d))
                    .y(d => getY(d))
                    .curve(d3.curveBundle);

                var node,
                    link;

                addParentNode(data);
                var root = stratify(data);
                cluster(root);
                var leaves = root.leaves();

                var g = svg.append("g")
                    .attr("transform", "translate(" + [diameter / 2, diameter / 2] + ")");

                node = g.append("g")
                    .selectAll("text")
                    .data(leaves)
                    .enter().append("text")
                    .attr("transform", d => "translate(" + [getX(d), getY(d)] + ") " + 
                        "rotate(" + (d.x * 180 / Math.PI - (isLeft(d) ? 180 : 0)) + ")")
                    .attr("text-anchor", d => isLeft(d) ? "end" : "start")
                    .attr("dx", d => isLeft(d) ? "-0.7em" : "0.7em")
                    .attr("dy", "0.3em")
                    .text(function(d) {
                        if(d.data.shortName[0] == '0' && d.data.shortName[1] == 'x') {
                            var startOfWalletID = d.data.shortName.substring(0,10);
                            startOfWalletID += ' ...'
                            return startOfWalletID
                        }
                        else {
                            var tempLabel = d.data.shortName.replaceAll("_", ".")
                            return tempLabel;
                        }
                    })
                    .on("mouseover", mouseovered)
                    .on("mouseout", mouseouted)
                    .on("click", function(d) {
                        if(d.data.shortName[0] == '0' && d.data.shortName[1] == 'x') {
                            window.location.replace("https://opensea.io/" + d.data.shortName)
                        }
                        else {
                            var nameInclFullstops = d.data.shortName.replaceAll("_", ".")
                            window.location.replace("https://opensea.io/" + nameInclFullstops)
                        }
                    });

                link = g.append("g")
                    .selectAll("path")
                    .data(getPaths(leaves))
                    .enter().append("path")
                    .each(d => { d.source = d[0]; d.target = d[d.length - 1]; })
                    .attr("d", line);

                function addParentNode(data) {
                    var map = {};
                    data.forEach(node => { map[node.name] = node; });

                    var node,
                        newNode,
                        index,
                        id;
                    for (var i = 0; i < data.length; i++) {
                        node = data[i];
                        index = node.name.lastIndexOf(".");
                        id = node.name.substring(0, index);
                        node.parentId = id;
                        node.shortName = node.name.substring(index + 1);
                        if (!map[id]) {
                            newNode = { name: id };
                            data.push(newNode);
                            map[id] = newNode;
                        }
                        // console.log(node.shortName)
                        // console.log(node.)
                    }
                    data.pop(); //remove the one with name "", since it causes multi-root error.
                }

                function getPaths(leaves) {
                    var map = {};
                    leaves.forEach(leaf => { map[leaf.data.name] = leaf; });

                    var paths = [];
                    leaves.forEach(leaf => {
                        leaf.data.imports.forEach(name => {
                            paths.push(leaf.path(map[name]));
                        });
                    });
                    return paths;
                }

                function mouseovered(d) {
                    node.each(n => { n.target = n.source = false; });
                    link.classed("link--target", l => { if (l.target === d) return l.source.source = true; })
                        .classed("link--source", l => { if (l.source === d) return l.target.target = true; })
                        .filter(l => l.target === d || l.source === d)
                        .raise();
                    node.classed("node--source", n => n.source)
                        .classed("node--target", n => n.target)
                    console.log(d3.selectAll(".link--target"));
                }

                function mouseouted(d) {
                    link.classed("link--source", false)
                        .classed("link--target", false);
                    node.classed("node--source", false)
                        .classed("node--target", false);
                }

                function getX(d) {
                    return d.y * Math.cos(d.x);
                }

                function getY(d) {
                    return d.y * Math.sin(d.x);
                }

                function isLeft(d) {
                    return d.x > Math.PI * 0.5 && d.x < Math.PI * 1.5;
                }
            }
        }
    }
</script>


<style>
    text {
        font: 12px Avenir;
    }
    
    text:hover,
    .node--source,
    .node--target {
        font-weight: bold;
    }
    
    text:hover {
        fill: black;
    }
    
    .node--source {
        fill: blue;
    }
    
    .node--target {
        fill: red;
    }
    
    path {
        fill: none;
        stroke: lightseagreen;
        stroke-width: 1px;
        opacity: 0.5;
    }
    
    .link--source, 
    .link--target {
        stroke-width: 2px;
        opacity: 1;
    }
    
    .link--source {
        stroke: red;
    }
    
    .link--target {
        stroke: blue;
    }

	/* 
    NOTE:
    
    RED = SALE
    BLUE = PURCHASE
    
    */
</style>