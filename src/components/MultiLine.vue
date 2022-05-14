<template>
    <div id="charts">
        <svg id="multiLineChart" width="1100" height="550"></svg>
    </div>
    <p>Timescale:</p>
    <form @submit="refreshMultiLine" class="radioGroup">
        <label for="month">1 Month<br />
            <input type="radio" id="month" value="month" name="timeframe">
        </label>
        <label for="week">3 Months<br />
            <input type="radio" id="3months" value="3months" name="timeframe" checked="checked">
        </label>
        <label for="day">6 Months<br />
            <input type="radio" id="6months" value="6months" name="timeframe">
        </label>
        <label for="year">1 Year<br />
            <input type="radio" id="year" value="year" name="timeframe">
        </label>
        <input type="submit" name="submit_button_2">
    </form>
</template>

<script>
    import * as d3 from 'd3'
    import axios from 'axios';

    export default {
        methods:
        {
            chart(evt)
            {
                const path = 'https://nft-back-end-py.herokuapp.com/get_line_graph_data';
                var request_json = ''
                if (evt == '')
                {
                    request_json = {'timeframe': '3months'}
                }
                else
                {
                    request_json = {'timeframe': evt.srcElement.timeframe.value}
                }

                axios.post(path, request_json, {timeout : 60000, maxContentLength : 100000000, maxBodyLength : 100000000})
                    .then((res) => {

		        var svg_reset = d3.select("#multiLineChart")
	    	        svg_reset.selectAll("*").remove()

		        var margin = {
		        top: 30, 	     
		        right: 50, 
		        bottom: 30, 
		        left: 50},
		        graphWidth = 850 - margin.left - margin.right,
		        graphHeight = 500 - margin.top - margin.bottom;

			var legendSpace = graphWidth / 8;
		      
		        // Append SVG to page
		        var svg = d3.select("#multiLineChart")
		      	  .append("svg")
		      	  .attr("graphWidth", graphWidth + margin.left + margin.right)
		      	  .attr("graphHeight", graphHeight + margin.top + margin.bottom)
		     		  .append("g")
			  .attr("transform", `translate(${margin.left}, ${margin.top})`);

                        var data = res.data

                        // Parse date / time
                        var parseTime = d3.timeParse("%Y-%m-%d");

                        // Set max Value for domain/ range 
                        var maxValue = d3.max(data, function(d) {
                                return Math.max(d.boredape, d.boredapekennel, d.clonex, d.coolcat, d.cryptoad, d. doodle, d.penguin, d.punk);})

                        // Set the ranges
                        var x = d3.scaleTime()
                                    .range([0, graphWidth]);
                        var y = d3.scaleLog()
                                    .domain([1, maxValue])
                                    .range([graphHeight, 1])
                                    .base(2);

                        // Define lines x8
                        var boredape = d3.line()
                            .x(function(d) { return x(d.timestamp); })
                            .y(function(d) { return y(d.boredape); })
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
                            .y(function(d) { return y(d.punk); });
                        
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
                        .attr("transform", `translate(${margin.left}, ${margin.top})`)
                        .attr("width", graphWidth)
                        .attr("height", graphHeight);
                        
                        svg.on("mouseout", hoverMouseOff)
                            .on("mouseover", hoverMouseOn)
                            .on("mousemove", hoverMouseOn);

                        // Add legend circles
                        svg.append("circle").attr("cx",850).attr("cy",40).attr("r", 6).style("fill", "black").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",60).attr("r", 6).style("fill", "blue").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",80).attr("r", 6).style("fill", "#FFD233").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",100).attr("r", 6).style("fill", "orange").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",120).attr("r", 6).style("fill", "red").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",140).attr("r", 6).style("fill", "purple").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",160).attr("r", 6).style("fill", "brown").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",180).attr("r", 6).style("fill", "green").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",200).attr("r", 6).style("fill", "gray").style("stroke", "black").attr('fill-opacity', 0.5)
                        svg.append("circle").attr("cx",850).attr("cy",220).attr("r", 6).style("fill", "white").style("stroke", "black").attr('fill-opacity', 0.5)

                        // Add legend text
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 40)
                        .text("Bored Ape Yacht Club")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var ba = d3.select('#boredapeline')
                            var active = ba.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#boredapeline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            ba.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 60)
                        .text("Bored Ape Kennel Club")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var bakc = d3.select('#boredapekennelline')
                            var active = bakc.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#boredapekennelline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            bakc.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 80)
                        .text("CloneX")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var cx = d3.select('#clonexline')
                            var active = cx.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#clonexline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            cx.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 100)
                        .text("CoolCats")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var cc = d3.select('#coolcatline')
                            var active = cc.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#coolcatline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            cc.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 120)
                        .text("CrypToadz")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var ct = d3.select('#cryptoadline')
                            var active = ct.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#cryptoadline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            ct.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 140)
                        .text("Doodles")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var dd = d3.select('#doodleline')
                            var active = dd.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#doodleline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            dd.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 160)
                        .text("Pudgy Penguins")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var pp = d3.select('#penguinline')
                            var active = pp.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#penguinline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            pp.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 180)
                        .text("CryptoPunks")
                        .style("font-size", "12px")
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var punk = d3.select('#punkline')
                            var active = punk.classed("active")
                            var new_opacity = active ? 0.5 : 0;
                            d3.select("#punkline")
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            punk.classed("active", !active);
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 200)
                        .text("All")
                        .style("font-size", "12px")
                        .style("font-weight", 600)
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var new_opacity = 0.5;
                            var a = d3.select('#boredapeline')
                            d3.select('#boredapeline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#boredapekennelline')
                            d3.select('#boredapekennelline')
                                    .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#clonexline')
                            d3.select('#clonexline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#coolcatline')
                            d3.select('#coolcatline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#cryptoadline')
                            d3.select('#cryptoadline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#doodleline')
                            d3.select('#doodleline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#penguinline')
                            d3.select('#penguinline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            a = d3.select('#punkline')
                            d3.select('#punkline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", false)
                            })
                        svg.append("text")
                        .attr("x", 870)
                        .attr("y", 220)
                        .text("None")
                        .style("font-size", "12px")
                        .style("font-weight", 600)
                        .attr("alignment-baseline","middle")
                        .on("click", function(){
                            var new_opacity = 0;
                            var a = d3.select('#boredapeline')
                            d3.select('#boredapeline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#boredapekennelline')
                            d3.select('#boredapekennelline')
                                    .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#clonexline')
                            d3.select('#clonexline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#coolcatline')
                            d3.select('#coolcatline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#cryptoadline')
                            d3.select('#cryptoadline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#doodleline')
                            d3.select('#doodleline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#penguinline')
                            d3.select('#penguinline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            a = d3.select('#punkline')
                            d3.select('#punkline')
                                .transition().duration(0)
                                .style("opacity", new_opacity)
                            a.classed("active", true)
                            })

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
                            if (!d0 || !d1)
                            {
                            return; //this was trying to find the date when hovering beyond the end of the graph
                            }
                            // work out which date value is closest to the mouse
                            var d = mouseDate - d0[0] > d1[0] - mouseDate ? d1 : d0;
                            boredapeLabel.text("Bored Ape Yacht Club: " + showValue(d.boredape))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y);
                            boredapekennelLabel.text("Bored Ape Kennel Club: " + showValue(d.boredapekennel))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 10);
                            clonexLabel.text("CloneX: " + showValue(d.clonex))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 20);
                            coolcatLabel.text("CoolCats: " + showValue(d.coolcat))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 30);
                            cryptoadLabel.text("CrypToadz: " + showValue(d.cryptoad))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 40);
                            doodleLabel.text("Doodles: " + showValue(d.doodle))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 50);
                            penguinLabel.text("Pudgy Penguins: " + showValue(d.penguin))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 60);
                            punkLabel.text("CryptoPunks: " + showValue(d.punk))
                                    .style('font', '10px Avenir')
                                    .attr('x', mouse_x + 10)
                                    .attr('y', mouse_y + 70);

                            hoverLine.attr("x1", mouse_x).attr("x2", mouse_x)
                            hoverLineGroup.style("opacity", 1);
                        }
                        function showValue(numericValue){
                            if(numericValue < 10) {
                                var decimalValue = Math.round((numericValue - 1) * 10)
                                return decimalValue / 10
                            }
                            else {
                                return Math.round(numericValue - 1)
                            }
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
                            y.domain([1, maxValue]);
                            
                            // Add the line paths 
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2) 
                                .style("stroke", "black")
                                .attr("class", "line")
                                .attr("d", boredape)
				.attr("id", "boredapeline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "blue")    
                                .attr("class", "line")
                                .attr("d", boredapekennel)
				.attr("id", "boredapekennelline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "#FFD233")    
                                .attr("class", "line")
                                .attr("d", clonex)
				.attr("id", "clonexline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "red")    
                                .attr("class", "line")
                                .attr("d", cryptoad)
				.attr("id", "cryptoadline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "purple")    
                                .attr("class", "line")
                                .attr("d", doodle)
				.attr("id", "doodleline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "orange")    
                                .attr("class", "line")
                                .attr("d", coolcat)
				.attr("id", "coolcatline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "brown")    
                                .attr("class", "line")
                                .attr("d", penguin)
				.attr("id", "penguinline");
                            svg.append("path")
                                .data([data])
                                .attr("transform", `translate(${margin.left}, ${margin.top})`)
                                .style("stroke-width", 2)
                                .style("stroke", "green")    
                                .attr("class", "line")
                                .attr("d", punk)
				.attr("id", "punkline");
                            
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
                                .text('Daily avg. transaction values,  (log₂ scale)')
                                .style('font', '18px Avenir')
                                .attr('fill', '#2c3e50')
                                .attr('transform', 'rotate(-90)')
                                .style('font-weight', 400);
                            svg.append('text')
                                .attr('text-anchor', 'middle')
                                .attr('y', 0)
                                .attr('x', margin.left + graphWidth/2)
                                .text('Daily average sale prices')
                                .style('font', '25px Avenir')
                                .attr('fill', '#2c3e50')
                                .style('font-weight', 600);

                            // Format ticks for both axes
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
            })
            .catch((error) => {
                console.error(error);
            });
        },
	refreshMultiLine(evt) {
	  evt.preventDefault()
	  this.chart(evt)
	}
	},
        mounted: function () {
            var evt = '';
            this.chart(evt)
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
.radioGroup label {
  display: inline-block;
  margin: 0 2.5em;
  text-align: center;
}
.radioGroup label input[type="radio"] {
  margin: 1em auto;
}
</style>
