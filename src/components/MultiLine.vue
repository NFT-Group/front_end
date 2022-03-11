<template>
    <div id="charts">
        <svg id="multiLineChart" width="900" height="600"></svg>
    </div>
</template>

<script>
    import * as d3 from 'd3'
    import data from '../../public/line_chart_data/multiline.json'
    console.log(data);

    export default {
        mounted: function () {
            function chart(data) {
                console.log(data)
                // Set dimensions
                var margin = {
                        top: 30, 
                        right: 50, 
                        bottom: 30, 
                        left: 50},
                    graphWidth = 850 - margin.left - margin.right,
                    graphHeight = 500 - margin.top - margin.bottom;

                // Append SVG to page
                var svg = d3.select("#multiLineChart")
                    .append("svg")
                    .attr("graphWidth", graphWidth + margin.left + margin.right)
                    .attr("graphHeight", graphHeight + margin.top + margin.bottom)
                    .append("g")
                    .attr("transform", `translate(${margin.left}, ${margin.top})`);


                // Parse date / time
                var parseTime = d3.timeParse("%Y-%m-%d");

                // Set the ranges
                var x = d3.scaleTime()
                            .range([0, graphWidth]);
                var y = d3.scaleLinear()
                            .range([graphHeight, 0]);

                // Define lines x8
                var boredape = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.boredape); });
                var boredapekennel = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.boredapekennel); });
                var clonex = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.clonex); });
                var coolcat = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.coolcat); });
                var cryptoad = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.cryptoad); });
                var doodle = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.doodle); });
                var penguin = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.penguin); });
                var punk = d3.line()
                    .x(function(d) { return x(d.timestamp); })
                    .y(function(d) { return y(d.boredapekennel); });
                
                // Add hover objects 
                var hoverLineGroup = svg.append("g")
                                    .attr("class", "hover-line");
                var hoverLine = hoverLineGroup
                    .append("line")
                        .attr("stroke", "#000")
                        .attr("x1", 10).attr("x2", 10)
                        .attr("y1", 0).attr("y2", graphHeight)
                        .attr("transform", `translate(0, ${margin.top})`);

                // Add labels
                var boredapeLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-tex capo")
                    .attr('dy', "0.35em");
                var boredapekennelLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var clonexLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var coolcatLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var cryptoadLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var doodleLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var penguinLabel = hoverLineGroup
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");
                var punkLabel = hoverLineGroup  
                    .append('text')
                    .attr("class", "hover-text capo")
                    .attr('dy', "0.35em");

                var rectHover = svg.append("rect")
                  .data(data)
                  .attr("fill", "none")
                  .attr("class", "overlay")
                  .attr("width", graphWidth)
                  .attr("height", graphWidth);

                svg.on("mouseout", hoverMouseOff)
                    .on("mousemove", hoverMouseOn);
                
                var bisectDate = d3.bisector(function(d) { return d.timestamp; }).left;
                
                function hoverMouseOn() {
                    var mouse_x = d3.mouse(this)[0];
                    var mouse_y = d3.mouse(this)[1];
                    var graph_y = y.invert(mouse_y);
                    var graph_x = x.invert(mouse_x);
                    var mouseDate = x.invert(mouse_x);
                    var i = bisectDate(data, mouseDate); // returns the index to the current data item
                    var d0 = data[i - 1]
                    var d1 = data[i];
                    // work out which date value is closest to the mouse
                    var d = mouseDate - d0[0] > d1[0] - mouseDate ? d1 : d0;
                    boredapeLabel.text("Bored Ape Yacht Club: " + Math.round(d.boredape))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y);
                    boredapekennelLabel.text("Bored Ape Kennel Club: " + Math.round(d.boredapekennel))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 10);
                    clonexLabel.text("Clonex: " + Math.round(d.clonex))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 20);
                    coolcatLabel.text("CoolCats: " + Math.round(d.coolcat))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 30);
                    cryptoadLabel.text("Cryptoadz: " + Math.round(d.cryptoad))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 40);
                    doodleLabel.text("Doodles: " + Math.round(d.doodle))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 50);
                    penguinLabel.text("Penguin: " + Math.round(d.penguin))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 60);
                    punkLabel.text("Punk: " + Math.round(d.boredapekennel))
                            .style('font', '10px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 70);

                    hoverLine.attr("x1", mouse_x).attr("x2", mouse_x)
                    hoverLineGroup.style("opacity", 1);
                }
                function hoverMouseOff() {
                        hoverLineGroup.style("opacity", 1e-6);
                }

                function renderGraph(data) {
                    // format the data
                    data.forEach(function(d) {
                        d.timestamp = parseTime(d.timestamp);
                        d.boredape = +d.boredape;
                        d.boredapekennel = +d.boredapekennel;
                        d.clonex = +d.clonex;
                        d.coolcat = +d.coolcat;
                        d.cryptoad = +d.cryptoad;
                        d.doodle = +d.doodle;
                        d.penguin = +d.penguin;
                        d.punk = +d.punk;
                    });
                    // Scale the range of the data
                    x.domain(d3.extent(data, function(d) { return d.timestamp; }));
                    y.domain([0, d3.max(data, function(d) {
                        // return Math.max(d.boredape, d.boredapekennel, d.clonex, d.coolcat, d.cryptoad, d. doodle, d.penguin, d.punk); })]);
                        return 150; })]);
                    
                    // Add the line paths 
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2) 
                        .style("stroke", "black")
                        .attr("class", "line")
                        .attr("d", boredape);
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "midnight-blue")    
                        .attr("class", "line")
                        .attr("d", boredapekennel);  
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "yellow")    
                        .attr("class", "line")
                        .attr("d", clonex);  
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "red")    
                        .attr("class", "line")
                        .attr("d", cryptoad);  
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "midnight-blue")    
                        .attr("class", "line")
                        .attr("d", doodle);
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "orange")    
                        .attr("class", "line")
                        .attr("d", coolcat);  
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "purple")    
                        .attr("class", "line")
                        .attr("d", penguin);
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 2)
                        .style("stroke", "green")    
                        .attr("class", "line")
                        .attr("d", punk); 
                    
                    // Add the X Axis
                    svg.append("g")
                        .attr("class", "Xaxis")
                        .attr("transform", `translate(${margin.left}, ${graphHeight + margin.top})`)
                        .call(d3.axisBottom(x));
                    // Add the Y Axis
                    svg.append("g")
                        .attr("class", "Yaxis")
                        .attr('fill', '#2c3e50')
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .call(d3.axisLeft(y)
                                .ticks(5));

                    // Add axis titles
                    svg.append('text')
                        .attr('text-anchor', 'middle')
                        .attr('y', 0)
                        .attr('x', -(margin.top) + -(graphHeight/2))
                        .text('Transaction value (ETH)')
                        .style('font', '18px Avenir')
                        .attr('fill', '#2c3e50')
                        .attr('transform', 'rotate(-90)')
                        .style('font-weight', 400);
                    svg.append('text')
                        .attr('text-anchor', 'middle')
                        .attr('y', 0)
                        .attr('x', margin.left + graphWidth/2)
                        .text('Average transaction values (All collections):')
                        .style('font', '25px Avenir')
                        .attr('fill', '#2c3e50')
                        .style('font-weight', 600);

                    // Format ticks for  both axes
                    d3.selectAll(".Xaxis>.tick>text")
                        .each(function(d, i){
                            d3.select(this).style("font-size", "14px")
                                            .attr('transform', 'rotate(20)')
                                            .attr('text-anchor', 'start');
                        });
                    d3.selectAll(".Yaxis>.tick>text")
                        .each(function(d, i){
                            d3.select(this).style("font-size", "14px")
                        });

                }
                renderGraph(data);
            };
            chart(data);
        } 
    }
</script>

<style>
.Xaxis line{ 
    stroke: black; 
}
.Xaxis path{ 
    stroke: black; 
}
.Yaxis line{ 
    stroke: black; 
}
.Yaxis path{ 
    stroke: black; 
}

</style>