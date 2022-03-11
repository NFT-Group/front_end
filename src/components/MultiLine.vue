<template>
    <div id="charts">
        <svg id="multiLineChart" width="900" height="600"></svg>
    </div>
</template>

<script>
    import * as d3 from 'd3'
    import data from '../../public/line_chart_data/multiLine.json'
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

                // Define collection lines 
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
                    .y(function(d) { return y(d.doodle); });]
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
                        .attr("transform", `translate(0, ${margin.top})`);;
                var hoverTT = hoverLineGroup.append('text')
                   .attr("class", "hover-tex capo")
                   .attr('dy', "0.35em");

                var hoverTT2 = hoverLineGroup.append('text')
                   .attr("class", "hover-text capo")
                   .attr('dy', "0.55em");

                var rectHover = svg.append("rect")
                  .data(data)
                  .attr("fill", "none")
                  .attr("class", "overlay")
                  .attr("width", graphWidth)
                  .attr("height", graphWidth);

                svg.on("mouseout", hoverMouseOff)
                    .on("mousemove", hoverMouseOn);
                
                var bisectDate = d3.bisector(function(d) { return d.Date; }).left;
                
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
                    hoverTT.text("Exports: " + Math.round(d.Exports))
                            .style('font', '12px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y);
                    hoverTT2.text("Imports: " + Math.round(d.Imports))
                            .style('font', '12px Avenir')
                            .attr('x', mouse_x + 10)
                            .attr('y', mouse_y + 10);
                    hoverLine.attr("x1", mouse_x).attr("x2", mouse_x)
                    hoverLineGroup.style("opacity", 1);
                }
                function hoverMouseOff() {
                        hoverLineGroup.style("opacity", 1e-6);
                }

                function renderGraph(data) {
                    // format the data
                    data.forEach(function(d) {
                        d.Date = parseTime(d.timestamp);
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
                    x.domain(d3.extent(data, function(d) { return d.Date; }));
                    y.domain([0, d3.max(data, function(d) {
                        return Math.max(d.Imports, d.Exports); })]);
                    
                    // Add the valueline path.
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 4) 
                        .style("stroke", "black")
                        .attr("class", "line")
                        .attr("d", valueline);
                    // Add the valueline path.
                    svg.append("path")
                        .data([data])
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .style("stroke-width", 4)
                        .style("stroke", "midnight-blue")    
                        .attr("class", "line")
                        .attr("d", valueline2);  



                    
                    // Add the X Axis
                    svg.append("g")
                        .attr("class", "axis")
                        .attr("transform", `translate(${margin.left}, ${graphHeight + margin.top})`)
                        .call(d3.axisBottom(x));
                    // Add the Y Axis
                    svg.append("g")
                        .attr("class", "axis")
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

                    // Set font for ticks 
                    d3.selectAll(".axis>.tick>text")
                        .each(function(d, i){
                            d3.select(this).style("font-size", "14px");
                        });

                }
                renderGraph(data, "Afghanistan");
            };
            chart(data);
        } 
    }
</script>

<style>
.axis line{ 
    stroke: black; 
}
.axis path{ 
    stroke: black; 
}


</style>