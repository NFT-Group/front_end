<template>
    <div id="Charts">
        <svg id="starterChart" width="700" height="500"></svg>
    </div>
</template>

<script>
  import * as d3 from 'd3'
  import { initializeApp } from 'firebase/app'
  import { getDatabase, ref, onValue, once, get } from "firebase/database";
  import { credentials, fisnapshottore, db } from 'firebase-admin'

    // CHART 1 - NFT COLLECTION COUNTS
  export default
  {
      mounted: function() {
            const firebaseConfig = {
                apiKey: "AIzaSyCMbegkc1LAvlUpj2akUiBr_I9lB2OW19k",
                authDomain: "practice-firebase-52292.firebaseapp.com",
                databaseURL: "https://practice-firebase-52292-default-rtdb.europe-west1.firebasedatabase.app",
                projectId: "practice-firebase-52292",
                storageBucket: "practice-firebase-52292.appspot.com",
                messagingSenderId: "481429582032",
                appId: "1:481429582032:web:de4d582b032c9d8ad6eed5",
                measurementId: "G-QBXC1HV2C0"
            };
            const app = initializeApp(firebaseConfig);

            // Get a reference to the database service
            const db = getDatabase(app);

            const svg = d3.select("#starterChart")
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

            // var data = [];
            // const starCountRef = ref(db, 'posts/' + postId + '/starCount');
            // onValue(starCountRef, (snapshot) => {
            // const data = snapshot.val();
            // onValue(starCountRef, (snapshot) => {
            //     updateStarCount(postElement, data);
            // });

            const reference = ref(db, 'practice-firebase-52292-default-rtdb');
            console.log(reference.once("size"))
            console.log(reference.get())
            console.log(reference);
            console.log("Hello")
            onValue(reference, (snapshot) => {
                console.log("Reference")
                data = snapshot.val()

                y.domain([0, d3.max(data, function(d) { return +d.size; })])
                    .range([graphHeight, 0]);
                x.domain(data.map(item => item.name))
                    .range([0, graphWidth])
                    .paddingInner(0.2)
                    .paddingOuter(0.2);

                const rects = graph.selectAll('rect').data(data);

                rects.exit().remove();

                rects.attr('width', x.bandwidth)                    
                    .attr('height', d => (graphHeight - y(d.size)))    
                    .attr('fill', 'midnightblue')              
                    .attr('x', d => x(d.name))                 
                    .attr('y', d => y(d.size));

                rects.enter()
                .append('rect')
                .attr('width', x.bandwidth)
                .attr('height', d => (graphHeight - y(d.size)))
                .attr('fill', 'midnightblue')
                .attr('x', d => x(d.name))
                .attr('y', d => y(d.size));   

                xAxisGroup.call(xAxis);        
                yAxisGroup.call(yAxis);

                            xAxisGroup.selectAll('text')
                .attr('transform', 'rotate(30)')
                .attr('text-anchor', 'start')
                .attr('fill', '#2c3e50')
                .style('font', '16px Avenir');

                yAxisGroup.selectAll('text')
                .attr('fill', '#2c3e50')
                .style('font', '16px Avenir');
            })
        console.log("End of function")
      }
  }
</script>

<style>
</style>