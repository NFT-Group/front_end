<template>
    <form @submit="onSubmit">
    <div class="label">
      <label>Choose a Collection:</label>
      </div>
        <select value="collection" id="collection" name="collection">
            <option value="punk" id="punk" name="collection">CryptoPunks</option>
            <option value="bored_ape_yacht_club" id="boredape" name="collection" selected="selected">Bored Ape Yacht Club</option>
            <option value="bored_ape_kennel_club" id="boredapekennel" name="collection">Bored Ape Kennel Club</option>
            <option value="doodles" id="doodle" name="collection">Doodles</option>
            <option value="cryptoadz" id="cryptoad" name="collection">CrypToadz</option>
            <option value="pudgy_penguins" id="penguin" name="collection">Pudgy Penguins</option>
            <option value="cool_cat" id="coolcat" name="collection">Cool Cats</option>
            <option value="cloneX" id="clonex" name="collection">cloneX</option>
        </select>
        <br><br>
        <input type="submit" name="submit_button">
    </form>

    <br> <p> Hover over wallet names/IDs to view transactions <br>
    Click on wallet names/IDs to visit OpenSea accounts </p> <br> 
    <div id="charts">
        <svg id="nodeChart" width="1350" height="1000"></svg>
    </div>
    <br><br>
    <h2>Suspicious trades in this collection:</h2>
    <div class="center-justified">
    <p> The whales identified above have been filtered to see if they are part of wash trading loops, and these loops are depicted below.      
        To identify suspicious transactions, we have isolated those that are part of a loop, e.g.: <br><br> 
        1) A --> B, B --> A <br>
        2) A --> B, B --> C, C --> A <br>
        3) A --> B, B --> C, C --> D, D --> A <br> <br>
        The NFT market has long been suspected to contain wash trading, and the charts below show that it is
        pervasive across NFT collections, some being significantly worse than others. <br> <br>
        Wallets names/IDs are connected in the graph below if they appear together in a loop.
        Clicking on wallet names/IDs will link you directly to OpenSea accounts.</p> <br> <br> 
    </div>
    <div id="charts">
        <svg id="loopsChart" width="1350" height="1000"></svg>
    </div>
    <br>
</template>

<script>
    // Import D3 & Grid.js
    import * as d3 from 'd3';

    import BAYCdata from '../../public/node_graph_data/bored_ape_yacht_club.json'
    import BAKCdata from '../../public/node_graph_data/bored_ape_kennel_club.json'
    import Ddata from  '../../public/node_graph_data/doodles.json'
    import CTdata from '../../public/node_graph_data/cryptoadz.json'
    import PPdata from '../../public/node_graph_data/pudgy_penguins.json'
    import CCdata from '../../public/node_graph_data/coolcat.json'
    import CXdata from '../../public/node_graph_data/clonex.json'
    import CPdata from '../../public/node_graph_data/punks.json'

    // Import Loop graph data 
    import BAYCLoopData from '../../public/loop_graph_data/bored_ape_yacht_club_loops.json'
    import BAKCLoopData from '../../public/loop_graph_data/bored_ape_kennel_club_loops.json'
    import DLoopData from '../../public/loop_graph_data/doodle_loops.json'
    import CTLoopData from '../../public/loop_graph_data/cryptoad_loops.json'
    import PPLoopData from '../../public/loop_graph_data/penguin_loops.json'
    import CCLoopData from '../../public/loop_graph_data/coolcat_loops.json'
    import CXLoopData from '../../public/loop_graph_data/clonex_loops.json'
    import CPLoopData from '../../public/loop_graph_data/punks_loops.json'

    export default {
        mounted: function () {
            // Set bored ape yacht club as default view 
            this.renderNodeChart('bored_ape_yacht_club');
            this.renderLoopsChart('bored_ape_yacht_club');
        },
        methods: {
            onSubmit(evt) {
                // Refresh SVG 
                evt.preventDefault();
                var svg_reset = d3.select("#nodeChart")
	            svg_reset.selectAll("*").remove()
                var svg_reset2 = d3.select("#loopsChart")
	            svg_reset2.selectAll("*").remove()
                var JSONname = evt.srcElement.collection.value
                // Render node chart
                this.renderNodeChart(JSONname)
                // Render loops chart
                this.renderLoopsChart(JSONname)

            },
            renderNodeChart(JSONname)
            {   
                var data;
                // Determine dataset from click 
                switch (JSONname){
                    case 'bored_ape_yacht_club':
                        data = BAYCdata;
                        break;
                    case 'bored_ape_kennel_club':
                        data = BAKCdata;
                        break;
                    case 'doodles':
                        data = Ddata;
                        break;
                    case 'cryptoadz':
                        data = CTdata;
                        break;
                    case 'pudgy_penguins':
                        data = PPdata;
                        break;
                    case 'punk':
                        data = CPdata;
                        break;
                    case 'cool_cats':
                        data = CCdata;
                        break;
                    case 'cloneX':
                        data = CXdata;
                        break;
                    default:
                        data = BAYCdata;
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


                // Add legend 
                svg.append("circle").attr("cx", 850).attr("cy",40).attr("r", 6).style("fill", "blue").attr('fill-opacity', 0.9)
                svg.append("circle").attr("cx", 850).attr("cy",60).attr("r", 6).style("fill", "red").attr('fill-opacity', 0.9)
                svg.append("text").attr("x", 844). attr("y", 20).text("On hover:").style("font-size", "12px").attr("alignment-baseline","middle").attr("text-anchor", "start").attr("font-weight", 800)
                svg.append("text").attr("x", 870).attr("y", 40).text("Purchase").style("font-size", "12px").attr("alignment-baseline","middle")
                svg.append("text").attr("x", 870).attr("y", 60).text("Sale").style("font-size", "12px").attr("alignment-baseline","middle")


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
                    }
                    data.pop(); 
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
            },
            renderLoopsChart(JSONname)
            {
                var data;
                // Determine dataset from click 
                switch (JSONname){
                    case 'bored_ape_yacht_club':
                        data = BAYCLoopData;
                        break;
                    case 'bored_ape_kennel_club':
                        data = BAKCLoopData;
                        break;
                    case 'doodles':
                        data = DLoopData;
                        break;
                    case 'cryptoadz':
                        data = CTLoopData;
                        break;
                    case 'pudgy_penguins':
                        data = PPLoopData;
                        break;
                    case 'punk':
                        data = CPLoopData;
                        break;
                    case 'cool_cats':
                        data = CCLoopData;
                        break;
                    case 'cloneX':
                        data = CXLoopData;
                        break;
                    default:
                        data = BAYCLoopData;
                }
                var diameter = 1000,
                innerCircle = 100,
                radius = diameter / 2 - innerCircle;

                var svg = d3.select("#loopsChart")
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
                        if(d.data.imports.length == 0)
                        {
                            return " ";
                        }
                        else
                        {
                            if(d.data.shortName[0] == '0' && d.data.shortName[1] == 'x') {
                                var startOfWalletID = d.data.shortName.substring(0,10);
                                startOfWalletID += ' ...'
                                return startOfWalletID
                            }
                            else {
                                var tempLabel = d.data.shortName.replaceAll("_", ".")
                                return tempLabel;
                            }
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
                    }
                    data.pop(); 
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
                    link.classed("link--target--loops", l => { if (l.target === d) return l.source.source = true; })
                        .classed("link--source--loops", l => { if (l.source === d) return l.target.target = true; })
                        .filter(l => l.target === d || l.source === d)
                        .raise();
                    node.classed("node--source--loops", n => n.source)
                        .classed("node--target--loops", n => n.target)
                }

                function mouseouted(d) {
                    link.classed("link--source--loops", false)
                        .classed("link--target--loops", false);
                    node.classed("node--source--loops", false)
                        .classed("node--target--loops", false);
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
    .link--source--loops {
        stroke: black;
    }
    .link--target--loops {
        stroke: black;
        stroke-width: 2px;
        opacity: 1;
    }
    .center-justified {
        text-align: justify;
        margin: 0 auto;
        width: 40em;
    }
    .search {
        font-size: 30px;
        font-family: Avenir;
        color: black;
    }
</style>
