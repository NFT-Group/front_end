<template>

  <h1>Quantum</h1>
  <p>AN NFT MARKET ANALYSER AND VISUALISER</p>
  <br><br>
  <p class="input">EXPLORE...</p>
  <form>
    <label>Blockchain:</label>
    <select >
        <option value="ethereum">Ethereum</option>
        <option value="solana">Solana</option>
    </select>
    <br>
    <label>Collection:</label>
    <select>
        <option value="allcollections">All Collection</option>
        <option value="cryptokittens">Crypto Kittens</option>
        <option value="boredapes">Bored Apes Yacht Club</option>
        <option value="littlelemon">Little Lemon</option>
        <option value="doodles">Doodles</option>
        <option value="artblocks">Art Blocks</option>
        <option value="cryptopunks">Crypto Punks</option>
        <option value="pudgypenguins">Pudgy Penguins</option>
        <option value="thesandbox">The Sandbox</option>
    </select>
    <br>
  </form>
</template>

<script>

  import * as d3 from 'd3'
  import { initializeApp } from 'firebase/app'
  import 'firebase/firestore'

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
  const db = app.firestore();

  function barcharts()
  {
      const svg = d3.select('.canvas')
      .append('svg')
      .attr('width', 600)
      .attr('height', 600);

      const margin = {
          top: 80,
          right: 20,
          bottom: 100,
          left: 140
      };

      const graphWidth = 600 - margin.left - margin.right;
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
          .tickFormat(d => d + ' NFTs');

      xAxisGroup.selectAll('text')
          .attr('transform', 'rotate(-30)')
          .attr('text-anchor', 'end')
          .attr('fill', '#2c3e50')
          .style('font', '16px Avenir');

      yAxisGroup.selectAll('text')
          .attr('fill', '#2c3e50')
          .style('font', '16px Avenir');

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
      db.collection('collections').onSnapshot(res => {
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
      })
  }

  barcharts()

</script>


<style>
  form{
    max-width: 420px; 
    margin: 20px auto; 
    background: white; 
    text-align: left;
    padding: 0px;
    border-radius: 10px;
  }
  label{
    color:#aaa;
    display: inline-block;
    margin: 25px 0 15px; 
    font-size: 0.6em;
    text-transform: uppercase;
    letter-spacing: 1px; 
    font-weight: bold; 
}
  input, select{
    display: block; 
    padding: 10px 6px;
    width: 100%;
    box-sizing: border-box;
    border: none; 
    border-bottom: 1px solid #ddd;
    color: #555;
  }
  input[type="checkbox"]{
    display: inline-block;
    width: 16px; 
    margin: 0 10px 0 0; 
    position: relative; 
    top: 2px; 
  }
  p.input{
    color: #444; 
    font-size: 1.2em; 
  }

</style>
