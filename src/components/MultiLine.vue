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
                var parseTime = d3.timeParse("%Y");

                // Set the ranges
                var x = d3.scaleTime()
                            .range([0, graphWidth]);
                var y = d3.scaleLinear()
                            .range([graphHeight, 0]);

                // Define collection lines 
                var valueline = d3.line()
                    .x(function(d) { return x(d.Date); })
                    .y(function(d) { return y(d.Imports); });
                var valueline2 = d3.line()
                    .x(function(d) { return x(d.Date); })
                    .y(function(d) { return y(d.Exports); });

                function renderGraph(data, country) {
                    var data = data[country];
                    
                    // format the data
                    data.forEach(function(d) {
                        d.Date = parseTime(d.Date);
                        d.Imports = +d.Imports;
                        d.Exports = +d.Exports;
                    });

                    // sort years ascending
                    data.sort(function(a, b){
                        return a["Date"]-b["Date"];
                        })
                    
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

                    // // Add axis titles
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