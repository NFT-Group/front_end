<template>
    <div id="charts">
        <svg id="barChart" width="700" height="500"></svg>
    </div>
</template>

<script>
import * as d3 from 'd3'
import { ref, onValue } from "firebase/database"
import { db } from '../assets/javascripts/firebaseConfig'

// CHART 1 - NFT COLLECTION COUNTS
export default {

    methods: {
        test() {
            console.log('test')
        },
        anotherTest() {
            console.log('hello')
        }
    },
    mounted: function() {

        this.test()
        
        const svg = d3.select("#barChart")
            .attr('width', 700)
            .attr('height', 500);

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
            .attr('y', graphHeight + margin.top + margin.bottom)
            .text('NFT Collections')
            .style('font', '18px Avenir')
            .attr('fill', '#2c3e50')
            .style('font-weight', 400);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('y', margin.left/3)
            .attr('x', -(margin.top) + -(graphHeight/2))
            .text('size of Collection (No. of NFTs)')
            .style('font', '18px Avenir')
            .attr('fill', '#2c3e50')
            .attr('transform', 'rotate(-90)')
            .style('font-weight', 400);

        svg.append('text')
            .attr('text-anchor', 'middle')
            .attr('y', margin.top/2)
            .attr('x', margin.left + graphWidth/2)
            .text('Transaction volumes in the past month')
            .style('font', '25px Avenir')
            .attr('fill', '#2c3e50')
            .style('font-weight', 600);

        const path = 'https://front-end-one-smoky.vercel.app/api/get_weeks_transactions';
        axios.get(path)
            .then((res) => {
                console.log(res)
                console.log(res.data)
                this.new_data(data)
                var data_array = [];
                var i = 0;
                for (; i < 8; i += 1)
                {
                    data_array[i] = data[toString(i)]
                }

                console.log("data_array")
                console.log(data_array)
                
                y.domain([0, d3.max(data_array, function(d) { return +d.size; })])
                    .range([graphHeight, 0])

                x.domain(data_array.map(item => item.name))
                    .range([0, graphWidth])
                    .paddingInner(0.2)
                    .paddingOuter(0.2)

                const rects = graph.selectAll('rect').data(data_array)

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