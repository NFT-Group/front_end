<template>
    <div id="Charts">
        <svg id="starterChart" width="900" height="600"></svg>
        <svg id="liveChart" width="900" height="600"></svg>
    </div>
</template>

<script>
  import * as d3 from 'd3'
  import { initializeApp } from 'firebase/app'
  import { getFirestore, collection, onSnapshot } from 'firebase/firestore'

    // CHART 1 - NFT COLLECTION COUNTS
  export default
  {
      mounted: function() {
          const firebaseConfig = {
                apiKey: "AIzaSyCMbegkc1LAvlUpj2akUiBr_I9lB2OW19k",
                authDomain: "practice-firebase-52292.firebaseapp.com",
                projectId: "practice-firebase-52292",
                storageBucket: "practice-firebase-52292.appspot.com",
                messagingSenderId: "481429582032",
                appId: "1:481429582032:web:de4d582b032c9d8ad6eed5",
                measurementId: "G-QBXC1HV2C0"
            };

            const app = initializeApp(firebaseConfig);
            const db = getFirestore();

            const svg = d3.select("#starterChart")
            .attr('width', 900)
            .attr('height', 600);

            const margin = {
                top: 80,
                right: 20,
                bottom: 100,
                left: 140
            };

            const graphWidth = 900 - margin.left - margin.right;
            const graphHeight = 600 - margin.top - margin.bottom;
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
                .text('Size of Collection (No. of NFTs)')
                .style('font', '18px Avenir')
                .attr('fill', '#2c3e50')
                .attr('transform', 'rotate(-90)')
                .style('font-weight', 400);

            svg.append('text')
                .attr('text-anchor', 'middle')
                .attr('y', margin.top/2)
                .attr('x', margin.left + graphWidth/2)
                .text('NFT Collections by Size')
                .style('font', '25px Avenir')
                .attr('fill', '#2c3e50')
                .style('font-weight', 600);

            var data = [];
            onSnapshot(collection(db, 'collections'), res => {
                res.docChanges().forEach(change => {
                    const doc = {...change.doc.data(), id: change.doc.id}
                    console.log(doc)
                    switch(change.type)
                    {
                        case 'added':
                            data.push(doc);
                            break;
                        case 'modified':
                            const index = data.findIndex(item => item.id == doc.id);
                            data[index] = doc;
                            break;
                        case 'removed':
                            data = data.filter(item => item.id !== doc.id);
                            break;
                        default:
                            break;
                    }
                })
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
                .attr('text-anchor', 'middle')
                .attr('fill', '#2c3e50')
                .style('font', '16px Avenir');

                yAxisGroup.selectAll('text')
                .attr('fill', '#2c3e50')
                .style('font', '16px Avenir');
            })
      }
  }
    // CHART 2 - LIVE UPDATE FROM BLOCKCHAIN
//   export default
//   {
//       mounted: function() {
//             const firebaseConfig = {
//             apiKey: "AIzaSyCpxt_NjEHYlZobU3f6NIGPqwLNzNYBVPs",
//             authDomain: "demonstration-99d81.firebaseapp.com",
//             projectId: "demonstration-99d81",
//             storageBucket: "demonstration-99d81.appspot.com",
//             messagingSenderId: "645635867507",
//             appId: "1:645635867507:web:605f29e5e8eb21546c3b06",
//             measurementId: "G-BDC6W0KT9P"
//             };

//             const app = initializeApp(firebaseConfig);
//             const db = getFirestore();

//             const svg = d3.select("#liveChart")
//             .attr('width', 900)
//             .attr('height', 600);

//             const margin = {
//                 top: 80,
//                 right: 20,
//                 bottom: 100,
//                 left: 140
//             };

//             const graphWidth = 900 - margin.left - margin.right;
//             const graphHeight = 600 - margin.top - margin.bottom;
//             const graph = svg.append('g')
//                 .attr('width', graphWidth)
//                 .attr('height', graphHeight)
//                 .attr('transform', `translate(${margin.left}, ${margin.top})`);

//             const xAxisGroup = graph.append('g')
//                 .attr('transform', `translate(0, ${graphHeight})`);
//             const yAxisGroup = graph.append('g');

//             const y = d3.scaleLinear()
//                 .range([graphHeight, 0]);
//             const x = d3.scaleBand()
//                 .range([0, graphWidth])
//                 .paddingInner(0.2)
//                 .paddingOuter(0.2);

//             const xAxis = d3.axisBottom(x);
//             const yAxis = d3.axisLeft(y)
//                 .ticks(5)
//                 .tickFormat(d => d);

//             xAxisGroup.selectAll('text')
//                 .attr('transform', 'rotate(30)')
//                 .attr('text-anchor', 'end')
//                 .attr('fill', '#2c3e50')
//                 .style('font', '20px Avenir');

//             yAxisGroup.selectAll('text')
//                 .attr('fill', '#2c3e50')
//                 .style('font', '20px Avenir');

//             svg.append('text')
//                 .attr('text-anchor', 'middle')
//                 .attr('x', graphWidth/2 + margin.left)
//                 .attr('y', graphHeight + margin.top + margin.bottom)
//                 .text('NFT Collections')
//                 .style('font', '18px Avenir')
//                 .attr('fill', '#2c3e50')
//                 .style('font-weight', 400);

//             svg.append('text')
//                 .attr('text-anchor', 'middle')
//                 .attr('y', margin.left/3)
//                 .attr('x', -(margin.top) + -(graphHeight/2))
//                 .text('No. of Transactions')
//                 .style('font', '18px Avenir')
//                 .attr('fill', '#2c3e50')
//                 .attr('transform', 'rotate(-90)')
//                 .style('font-weight', 400);

//             svg.append('text')
//                 .attr('text-anchor', 'middle')
//                 .attr('y', margin.top/2)
//                 .attr('x', margin.left + graphWidth/2)
//                 .text('Number of Transactions since Feb 18 2022 @ 10am')
//                 .style('font', '25px Avenir')
//                 .attr('fill', '#2c3e50')
//                 .style('font-weight', 600);

//             var data = [];
//             onSnapshot(collection(db, 'collections'), res => {
//                 res.docChanges().forEach(change => {
//                     const doc = {...change.doc.data(), id: change.doc.id}
//                     console.log(doc)
//                     switch(change.type)
//                     {
//                         case 'added':
//                             data.push(doc);
//                             break;
//                         case 'modified':
//                             const index = data.findIndex(item => item.id == doc.id);
//                             data[index] = doc;
//                             break;
//                         case 'removed':
//                             data = data.filter(item => item.id !== doc.id);
//                             break;
//                         default:
//                             break;
//                     }
//                 })
//                 y.domain([0, d3.max(data, function(d) { return +d.size; })])
//                     .range([graphHeight, 0]);
//                 x.domain(data.map(item => item.name))
//                     .range([0, graphWidth])
//                     .paddingInner(0.2)
//                     .paddingOuter(0.2);

//                 const rects = graph.selectAll('rect').data(data);

//                 rects.exit().remove();

//                 rects.attr('width', x.bandwidth)                    
//                     .attr('height', d => (graphHeight - y(d.size)))    
//                     .attr('fill', 'midnightblue')              
//                     .attr('x', d => x(d.name))                 
//                     .attr('y', d => y(d.size));

//                 rects.enter()
//                 .append('rect')
//                 .attr('width', x.bandwidth)
//                 .attr('height', d => (graphHeight - y(d.size)))
//                 .attr('fill', 'midnightblue')
//                 .attr('x', d => x(d.name))
//                 .attr('y', d => y(d.size));   

//                 xAxisGroup.call(xAxis);        
//                 yAxisGroup.call(yAxis);
//             })
//       }
//   }

</script>


<style>
</style>