// SET UP GRAPH ------------------------------------------------------------------
// Select canvas container and append SVG
const svg = d3.select('.canvas')
    .append('svg')
        .attr('width', 600)
        .attr('height', 600);

// Create margins and dimensions
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
    .attr('transform', `translate(${margin.left}, ${margin.top})`);     // Displaces graph from being flush with top-left of screen

// Create axes groups
const xAxisGroup = graph.append('g')
    .attr('transform', `translate(0, ${graphHeight})`);
const yAxisGroup = graph.append('g');

// Set up axes (without domain)
const y = d3.scaleLinear()
    .range([graphHeight, 0]);                           // Range of scale on graph
const x = d3.scaleBand()
    .range([0, graphWidth])
    .paddingInner(0.2)
    .paddingOuter(0.2);

// Create & call the axes
const xAxis = d3.axisBottom(x);
const yAxis = d3.axisLeft(y)
    .ticks(5)
    .tickFormat(d => d + ' NFTs');

// Set axis text
xAxisGroup.selectAll('text')
    .attr('transform', 'rotate(-30)')
    .attr('text-anchor', 'end')
    .attr('fill', '#2c3e50')
    .style('font', '16px Avenir');

yAxisGroup.selectAll('text')
    .attr('fill', '#2c3e50')
    .style('font', '16px Avenir');

// Add axis titles
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

// Add axis graph title
svg.append('text')
    .attr('text-anchor', 'middle')
    .attr('y', margin.top/2)
    .attr('x', margin.left + graphWidth/2)
    .text('NFT Collections by Size')
    .style('font', '25px Avenir')
    .attr('fill', '#2c3e50')
    .style('font-weight', 600);


// UPDATE FUNCTION ------------------------------------------------------------
const update = (data) => {
    // Update scale domains
    y.domain([0, d3.max(data, function(d) { return +d.size; })])    // Spread of actual datapoints (responseive not hard coded)
        .range([graphHeight, 0]);                                   // Range of scale on graph
    x.domain(data.map(item => item.name))                           // Map() cycles through the JSON array and returns an array of all the 'name' variables
        .range([0, graphWidth])
        .paddingInner(0.2)
        .paddingOuter(0.2);
    // Join updated data to elements
    const rects = graph.selectAll('rect').data(data);
    // Remove unwanted (if any) shapes using exit selection
    rects.exit().remove();
    // Update the rectangle(s) already in the DOM
    rects.attr('width', x.bandwidth)                        // Sets standard bar width
        .attr('height', d => (graphHeight - y(d.size)))     // Sets height of bars (passed through the y scale)
        .attr('fill', 'midnightblue')                       // Sets fill for bars
        .attr('x', d => x(d.name))                          // Sets bar spacing
        .attr('y', d => y(d.size));
    // Append the enter selection to the DOM
    rects.enter()
    .append('rect')
    .attr('width', x.bandwidth)
    .attr('height', d => (graphHeight - y(d.size)))
    .attr('fill', 'midnightblue')
    .attr('x', d => x(d.name))
    .attr('y', d => y(d.size));   
    // Call axes
    xAxisGroup.call(xAxis);                     // Runs the axis function on the group, generating the SVGs and adding them to group
    yAxisGroup.call(yAxis);
}

// Declare data array
var data = [];
// Listen to firebase database ('onSnapshot' fires every time database changes)
db.collection('collections').onSnapshot(res => {
    res.docChanges().forEach(change => {
        // Set ID from firebase for each data point 
        const doc = {...change.doc.data(), id: change.doc.id}
        // Switch statement to decide between new, modified and deleted data
        switch(change.type)
        {
            case 'added':
                data.push(doc);
                break;
            case 'modified':
                // Find index of item inside data array
                const index = data.findIndex(item => item.id == doc.id);
                data[index] = doc;
                break;
            case 'removed':
                // Filters all data points for items with ID 
                data = data.filter(item => item.id !== doc.id);
                break;
            default:
                break;
        }
    })
    update(data);
})

