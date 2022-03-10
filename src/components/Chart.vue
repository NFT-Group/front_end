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
            .text('NFT Collections by size')
            .style('font', '25px Avenir')
            .attr('fill', '#2c3e50')
            .style('font-weight', 600);

        const reference = db.ref('/');

        var apeAddress = '0xBC4CA0EdA7647A8aB7C2061c2E118A18a936f13D'
        var cryptoPunkAddress = '0xb47e3cd837dDF8e4c57F05d70Ab865de6e193BBB'
        var doodlesAddress = '0x8a90CAb2b38dba80c64b7734e58Ee1dB38B8992e'
        var coolCatsAddress = '0x1A92f7381B9F03921564a437210bB9396471050C'
        var cloneXAddress = '0x49cF6f5d44E70224e2E23fDcdd2C053F30aDA28B'
        var crypToadzAddress = '0x1CB1A5e65610AEFF2551A50f76a87a7d3fB649C6'
        var boredApeKennelAddress = '0xba30E5F9Bb24caa003E9f2f0497Ad287FDF95623'
        var pudgyPenguinAddress = '0xBd3531dA5CF5857e7CfAA92426877b022e612cf8'

        onValue(reference, (snapshot) => {
            //const data = Object.values(snapshot.val())
            //console.log(data)

            //get number of historical transactions for all collections
            //format data into Array object of 8 elements with 'name' and 'size' fields
            var last_month_transactions = reference.orderByChild('timestamp').startAt('2022-02-10').get() //make this less hard coded!!
            console.log(last_month_transactions)
            var collection_names = ['Bored Ape Yacht Club', 'CryptoPunks', 'Bored Ape Kennel Club', 'Cool Cats', 'cloneX', 'CrypToadz', 'Doodles', 'Pudgy Penguins'];
            var total_transaction_counts = [0, 0, 0, 0, 0, 0, 0, 0];
            var transaction_keys = Object.keys(last_month_transactions);
            var i = 0;
            for (; i < transaction_keys.length; i += 1)
            {
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == apeAddress) { total_transaction_counts[0] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == cryptoPunkAddress) { total_transaction_counts[1] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == boredApeKennelAddress) { total_transaction_counts[2] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == coolCatsAddress) { total_transaction_counts[3] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == cloneXAddress) { total_transaction_counts[4] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == crypToadzAddress) { total_transaction_counts[5] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == doodlesAddress) { total_transaction_counts[6] += 1 };
                if (last_month_transactions[transaction_keys[i]]['contracthash'] == pudgyPenguinAddress) { total_transaction_counts[7] += 1 };
            }

            console.log(collection_names)
            console.log(total_transaction_counts)

            var data = [];
            var i = 0;
            for (; i < 8; i += 1)
            {
                data_array[i] = { 'name' : collection_names[i], 'size' : total_transaction_counts[i] }
            }

            data

            console.log("data")
            console.log(data)
            
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
      }

  }
</script>

<style>
</style>