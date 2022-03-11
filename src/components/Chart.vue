<template>
    <div id="charts">
        <svg id="barChart" width="750" height="500"></svg>
    </div>
</template>

<script>
import * as d3 from 'd3'
import { ref, onValue } from "firebase/database"
//import { db } from '../assets/javascripts/firebaseConfig'
import axios from 'axios';

// CHART 1 - NFT COLLECTION COUNTS
export default {
    mounted: function() {
        
        const svg = d3.select("#barChart")
            .attr('width', 750)
            .attr('height', 700);

        const margin = {
            top: 80,
            right: 20,
            bottom: 100,
            left: 140
        }; 

        const graphWidth = 700 - margin.left - margin.right;
        const graphHeight = 500 - margin.top - margin.bottom;
        const graph = svg.append('g')
            .attr('width', graphWidth)
            .attr('height', graphHeight)
            .attr('transform', `translate(${margin.left}, ${margin.top})`);

        const xAxisGroup = graph.append('g')
            .attr('transform', `translate(0, ${graphHeight})`);
        const yAxisGroup = graph.append('g');

        const y = d3.scaleLinear()
            .range([graphHeight, 0]);
        const x = d3.scaleBand()
            .range([0, graphWidth])
            .paddingInner(0.2)
            .paddingOuter(0.2);

        const xAxis = d3.axisBottom(x);
        const yAxis = d3.axisLeft(y)
            .ticks(5)
            .tickFormat(d => d);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('x', graphWidth/2 + margin.left)
            .attr('y', graphHeight + margin.top + margin.bottom + (margin.bottom/2))
            .text('NFT Collection')
            .style('font', '18px Avenir')
            .attr('fill', '#2c3e50')
            .style('font-weight', 400);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('y', margin.left/3)
            .attr('x', -(margin.top) + -(graphHeight/2))
            .text('No. of transactions')
            .style('font', '18px Avenir')
            .attr('fill', '#2c3e50')
            .attr('transform', 'rotate(-90)')
            .style('font-weight', 400);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('y', margin.top/2)
            .attr('x', margin.left + graphWidth/2)
            .text('Transaction Volumes (Past 30 days)')
            .style('font', '25px Avenir')
            .attr('fill', '#2c3e50')
            .style('font-weight', 600);

        const path = 'https://front-end-one-smoky.vercel.app/api/get_weeks_transactions';
        axios.get(path)
            .then((res) => {
                console.log(res)
                console.log(res.data)

                var data = res.data
                
                y.domain([0, d3.max(data, function(d) { return +d.size; })])
                    .range([graphHeight, 0])

                x.domain(data.map(item => item.name))
                    .range([0, graphWidth])
                    .paddingInner(0.2)
                    .paddingOuter(0.2)

                const rects = graph.selectAll('rect').data(data)

                rects.exit().remove()

                rects.attr('width', x.bandwidth)                    
                    .attr('height', d => (graphHeight - y(d.size)))    
                    .attr('fill', 'midnightblue')              
                    .attr('x', d => x(d.name))                 
                    .attr('y', d => y(d.size))
                    
                rects.enter()
                    .append('rect')
                    .attr('width', x.bandwidth)
                    .attr('height', d => (graphHeight - y(d.size)))
                    .attr('fill', 'midnightblue')
                    .attr('x', d => x(d.name))
                    .attr('y', d => y(d.size))   
                
                xAxisGroup.call(xAxis)       
                yAxisGroup.call(yAxis)
                
                xAxisGroup.selectAll('text')
                    .attr('transform', 'rotate(30)')
                    .attr('text-anchor', 'start')
                    .attr('fill', '#2c3e50')
                    .style('font', '16px Avenir')

                yAxisGroup.selectAll('text')
                    .attr('fill', '#2c3e50')
                    .style('font', '16px Avenir')
            })
            .catch((error) => {
                console.error(error);
            });
      }

  }
</script>

<style>
</style>