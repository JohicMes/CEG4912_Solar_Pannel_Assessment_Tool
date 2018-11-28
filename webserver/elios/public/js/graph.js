// Inspired from https://bl.ocks.org/d3noob/402dd382a51a4f6eea487f9a35566de0
// "simple line graph with v4 by d3noob"
// Load the data from our restful api
d3.json('http://localhost/api/solar/').then(function(data) {
    //Convert the data to date and int respectively
    data.forEach(function(d){
        d.time = d3.timeParse("%Y-%m-%d %H:%M:%S")(d.time);
        d.intensity = +d.intensity;
        delete d.id;
        delete d.created_at;
        delete d.updated_at;
    });


    var margin = {top: 20, right: 20, bottom: 30, left: 50};
    
    var width = 960 - margin.left - margin.right,
        height = 500 - margin.top - margin.bottom;

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
    .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top +")");
    

    var x = d3.scaleTime()
        .domain(d3.extent(data, function(d) { return d.time; }))
        .range([0, width]);

    var y = d3.scaleLinear()
        .domain([0, d3.max(data, function(d) { return d.intensity; })])
        .range([height, 0]);


    var line = d3.line()
        .x(function(d) { return x(d.time);})
        .y(function(d) { return y(d.intensity); });

    var svg = d3.select("body").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    svg.append("path")
        .datum(data)
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 1.5)
        .attr("stroke-linejoin", "round")
        .attr("stroke-linecap", "round")
        .attr("d", line);

    // Add axis
    svg.append("g")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(x));

    svg.append("g")
        .call(d3.axisLeft(y));

    console.log("Hello!!!");


});
