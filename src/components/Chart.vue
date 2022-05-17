<template>

    <div id="charts">
        <svg id="barChart" width="750" height="510"></svg>
    </div>
    <p>Select Volume or Cumulative Value against preferred timescale:</p>
    <form @submit="refreshData" class="radioGroup">
		<label for="volume">Volume<br />
			<input type="radio" id="volume" value="volume" name="data_type" checked="checked">
		</label>
		<label for="price">Cumulative value<br />
			<input type="radio" id="cumulative_value" value="cumulative_value" name="data_type">
		</label>
		<br>
		<label for="day">Day<br />
			<input type="radio" id="day" value="day" name="timeframe">
		</label>
		<label for="week">Week<br />
			<input type="radio" id="week" value="week" name="timeframe" checked="checked">
		</label>
		<label for="month">Month<br />
			<input type="radio" id="month" value="month" name="timeframe">
		</label>
		<input type="submit" name="submit_button">
    </form>
</template>

<script>
import * as d3 from 'd3'
import axios from 'axios';

// CHART 1 - NFT COLLECTION COUNTS
export default {
    methods: {
      buildBarChart(evt) {
	
        const path = 'https://front-end-one-smoky.vercel.app/api/get_transactions';
		var request_json = ''
		
		if (evt == '') {
			request_json = {'timeframe': 'week', 'data_type': 'volume'}
		}
		else {
			request_json = {'timeframe': evt.srcElement.timeframe.value, 'data_type': evt.srcElement.data_type.value}
		}
        axios.post(path, request_json)
            .then((res) => {
            	var data = res.data
				var svg_reset = d3.select("#barChart")
				svg_reset.selectAll("*").remove()
				
				const svg = d3.select("#barChart")
					.attr('width', 750)
					.attr('height', 510);

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

				if(request_json.data_type == 'volume') {
					svg.append('text')
					.attr('text-anchor', 'middle')
					.attr('y', margin.left/3)
					.attr('x', -(margin.top) + -(graphHeight/2))
					.text('Sale volume')
					.style('font', '18px Avenir')
					.attr('fill', '#2c3e50')
					.attr('transform', 'rotate(-90)')
					.style('font-weight', 400);
				} else {
					svg.append('text')
					.attr('text-anchor', 'middle')
					.attr('y', margin.left/3)
					.attr('x', -(margin.top) + -(graphHeight/2))
					.text('Cumulative value of sales')
					.style('font', '18px Avenir')
					.attr('fill', '#666e77')
					.attr('transform', 'rotate(-90)')
					.style('font-weight', 400);
				}

				svg.append('text')
					.attr('text-anchor', 'middle')
					.attr('y', margin.top/2)
					.attr('x', margin.left + graphWidth/2)
					.text('Cumulative overview')
					.style('font', '25px Avenir')
					.attr('fill', '#666e77')
							.style('font-weight', 600);

					
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
					.attr('x', d => x(d.name))                 
					.attr('y', d => y(d.size))
					
				rects.enter()
					.append('rect')
					.attr('width', x.bandwidth)
					.attr('height', d => (graphHeight - y(d.size)))
					.attr('fill', function(d) { 
						switch (d.name){
						case 'Bored Ape Yacht Club':
							return "black";
						case 'Bored Ape Kennel Club':
							return "blue";
						case 'cloneX':
							return "#FFD233";
						case 'Cool Cats':
							return "orange";
						case 'CrypToadz':
							return "red";
						case 'Doodles':
							return "purple";
						case 'Pudgy Penguins':
							return "brown";
						case 'CryptoPunks':
							return "green";
						default:
							return "black";
					}})
					.attr("fill-opacity", 0.7)  
					.attr('x', d => x(d.name))
					.attr('y', d => y(d.size))   
				
				xAxisGroup.call(xAxis)
							.attr("class", "Xaxis");       
				yAxisGroup.call(yAxis)
							.attr("class", "Yaxis");
				
				xAxisGroup.selectAll('text')
					.attr('transform', 'rotate(30)')
					.attr('text-anchor', 'start')
					.attr('fill', '#2c3e50')
					.style('font', '14px Avenir');

				yAxisGroup.selectAll('text')
					.attr('fill', '#2c3e50')
					.style('font', '14px Avenir');
				})
				.catch((error) => {
					console.error(error);
				});
      },
      refreshData(evt) {
        evt.preventDefault()
        this.buildBarChart(evt)
      }
    },
    mounted: function() {
    	var evt = ''
        this.buildBarChart(evt)
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
.radioGroup {
	text-align: center;
}
.radioGroup label {
  display: inline-block;
  margin: 0.2em;
  margin-left: 10em;
  text-align: center;
}
.radioGroup label input[type="radio"] {
	display: inline-block;	
	margin-left: 10em;
  	margin: 1em auto;
} 
</style>
