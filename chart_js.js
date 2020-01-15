
var CHART = document.getElementById("linechart");
console.log(CHART);

const data = []

d3.csv("resources\final_data.csv").then(function (d) {
    console.log(d[0]);
    var dateTime = 'DD/MM/YYYY';

    d.forEach(function (item) {
        data.push({
            x: item.Date,
            y: item.Weighted_Avg_Price
        })
    });

    //   console.log(data)
    var lineChart = new Chart(CHART, {
        type: 'line',
        label: 'Commodity',
        data: data
});
