const renderChart = (data, labels) => {

    var ctx = document.getElementById('myChart').getContext('2d');
    var chart = new Chart(ctx, {
        // The type of chart we want to create
        type: 'doughnut',

        // The data for our dataset
        data: {
            labels: labels,
            datasets: [{
                label: 'Last 6 months expenses',
                backgroundColor: 'rgb(255, 99, 132)',
                borderColor: 'rgb(255, 99, 132)',
                data: data
            }]
        },

        // Configuration options go here
        options: {
            title: {
                display:true,
                text:'Expenses by category'
            }
        }
    });
};

const getChartData = () => {
    fetch('expense_category_summary')
    .then((res) => res.json())
    .then((results) => {
        console.log('results', results);
        const category_data = results.expense_category_data;
        const [labels, data] = [
            Object.keys(category_data),
            Object.values(category_data)
        ]

        renderChart(data, labels)
    });
};

document.onload = getChartData();