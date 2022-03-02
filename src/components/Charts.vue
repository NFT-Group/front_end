<template>
  <div class="charts">
    <div id="bloodGroupChart"></div>
    <div id="ageRangesChart"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';
export default {
  name: 'Charts',
  props: {
    patients: {
      type: Array,
      validator: (patient) => patient.every(x => typeof x === 'object'),
      required: true
    }
  },
  data: ()=> {
    return {
      width: 360,
      height: 280,
      margin: {top: 50, right: 50, bottom: 50, left: 50}
    }
  },
  computed: {
    groupCounts(){
      let groupCounts = {};
      this.patients.map(patient => {
        groupCounts[patient.bloodgroup] = groupCounts[patient.bloodgroup] + 1 || 1;  
      })
      return groupCounts;
    },
    bloodGroups(){
      return Object.keys(this.groupCounts)
    },
    ageRanges(){
      let ageRanges = {};
      this.patients.map(patient => {
        if(patient.age < 18){
          ageRanges['Under 18'] = ageRanges['Under 18'] + 1 || 1
        } else if(patient.age < 30){
          ageRanges['18-30yrs'] = ageRanges['18-30yrs'] + 1 || 1
        } else if(patient.age < 60){
          ageRanges['30-60yrs'] = ageRanges['30-60yrs'] + 1 || 1
        } else {
          ageRanges['Over 60'] = ageRanges['Over 60'] + 1 || 1
        }
      })
      return ageRanges;
    },
    ageGroups(){
      return Object.keys(this.ageRanges)
    }
  },
  methods: {
    initBloodGroupChart(){
      var width = this.width - this.margin.left - this.margin.right,
      height = this.height - this.margin.top - this.margin.bottom,
      margin = this.margin;


      var x = d3.scaleBand()
      .range([0, width])
      .padding(0.1);
      var y = d3.scaleLinear()
      .range([height, 0]);
          
      var svg = d3.select("#bloodGroupChart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .style("border", "3px solid black")
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      var data = [...this.bloodGroups].map((group)=>{
        return {bloodgroup: group, count: this.groupCounts[group]};
      });

      x.domain(data.map(function(d) { return d.bloodgroup; }));
      y.domain([0, d3.max(data, function(d) { return d.count; })]);

      svg.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .style("fill", "steelblue")
      .attr("x", function(d) { return x(d.bloodgroup); })
      .attr("width", x.bandwidth())
      .attr("y", function(d) { return y(d.count); })
      .attr("height", function(d) { return height - y(d.count); });

      svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
      .append("text")
      .attr("y", height - 150)
      .attr("x", width - 100)
      .attr("text-anchor", "end")
      .attr("stroke", "black")
      .text("Blood Group");

      svg.append("g")
      .call(d3.axisLeft(y))
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "-3.1em")
      .attr("text-anchor", "end")
      .attr("stroke", "black")
      .text("Number of Patients with Blood Group");

      svg.append("text")
      .attr("transform", "translate(80,-10)")
      .attr("x", 0)
      .attr("y", 0)
      .attr("font-size", "20px")
      .text("Blood Groups");
    },
    initAgeRangesChart(){
      var width = this.width - this.margin.left - this.margin.right,
      height = this.height - this.margin.top - this.margin.bottom,
      margin = this.margin;


      var x = d3.scaleBand()
      .range([0, width])
      .padding(0.1);
      var y = d3.scaleLinear()
      .range([height, 0]);
          
      var svg = d3.select("#ageRangesChart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .style("border", "3px solid black")
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
      
      var data = [...this.ageGroups].map((group)=>{
        return {agerange: group, count: this.ageRanges[group]};
      });

      x.domain(data.map(function(d) { return d.agerange; }));
      y.domain([0, d3.max(data, function(d) { return d.count; })]);

      svg.selectAll(".bar")
      .data(data)
      .enter().append("rect")
      .style("fill", "steelblue")
      .attr("x", function(d) { return x(d.agerange); })
      .attr("width", x.bandwidth())
      .attr("y", function(d) { return y(d.count); })
      .attr("height", function(d) { return height - y(d.count); });

      svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x))
      .append("text")
      .attr("y", height - 150)
      .attr("x", width - 100)
      .attr("text-anchor", "end")
      .attr("stroke", "black")
      .text("Age Range");

      svg.append("g")
      .call(d3.axisLeft(y))
      .append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "-3.1em")
      .attr("text-anchor", "end")
      .attr("stroke", "black")
      .text("Number of Patients in Age Range");

      svg.append("text")
      .attr("transform", "translate(80,-10)")
      .attr("x", 0)
      .attr("y", 0)
      .attr("font-size", "20px")
      .text("Age Distribution");
    }
  },
  mounted(){
    this.initBloodGroupChart();
    this.initAgeRangesChart();
  }
}
</script>

<style scoped>
</style>


