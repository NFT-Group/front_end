<template>
    <div id="charts">
        <svg id="nodeChart" width="1350" height="1000"></svg>
    </div>
</template>

<script>
    import * as d3 from 'd3';
    import { ethers } from 'ethers';
    import * as ENS from 'ethereum-ens';
    import * as Web3 from 'web3';
    import data from '../../public/node_graph_data/boredApeYachtClub.json'

    export default {
            mounted: function() {
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

            // async function findName(name) {
            //     var infuraUrl = 'https://mainnet.infura.io/v3/28b465e090554529bb7913d0504a71bd';
            //     var provider = new ethers.providers.JsonRpcProvider(infuraUrl);
            //     var address = await provider.lookupAddress(name);
            //     if(address == null)
            //     {
            //         address = name.substring(0,8);
            //         address += "...";
            //     }
            //     console.log(address)
            //     return address
            // }
            // var example = "0x4e064ddcc82194c12c7ff5712a6e1938aee9abe8";
            // var example2 = "0x5555763613a12D8F3e73be831DFf8598089d3dCa";
            // findName(example);
            // findName(example2);

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