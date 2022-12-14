//sidebar code
const gainers = document.getElementById('myChart').getContext('2d');
const losers = document.getElementById('topLosers').getContext('2d');
const time = document.querySelector(".time")
const name_grow =  document.querySelectorAll(".commodity_name_grow")
const price_grow = document.querySelectorAll(".commodity_price_price")
const name_loose = document.querySelectorAll(".top_loser_name")
const price_loose = document.querySelectorAll(".top_loser_price")
//const time_commo = document.querySelectorAll(".time_commo")
//getting name_grow
let productArr = []
for (let val = 0; val < name_grow.length; val++) {
    productArr.push(name_grow[val].textContent)
}
//getting name_grow
let loserProductArr = []
for (let val = 0; val < name_loose.length; val++) {
    loserProductArr.push(name_loose[val].textContent)
}
//getting price grow
let priceArr = []
for (let val = 0; val < price_grow.length; val++) {
    priceArr.push(Math.floor(Number(price_grow[val].textContent)/100))
}
//getting price loose
let loosePriceArr = []
for (let val = 0; val < price_loose.length; val++) {
    loosePriceArr.push(Math.floor(Number(price_loose[val].textContent)/100))
}
console.log(loosePriceArr)
const topGainers = new Chart(gainers, {
    type: 'bar',
    data: {
        
        labels: productArr,
        datasets: [{
            label: 'Commodities Which gained highest price',
            data: priceArr,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(0, 0, 0, 0.4)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(0, 0, 0, 1)',
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const topLosers  = new Chart(losers,{
    type: 'bar',
    data: {
        labels:loserProductArr,
        datasets: [{
            label: 'Commodities Which gained highest price',
            data: loosePriceArr,
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
})

//fetching date

function getDate() {
    let dateArray = [
        "Sunday",
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday"
        
    ]
    let time = dateFns.format(new Date(),"hh:mm:ssa")
    let day = dateArray[dateFns.getDay(new Date())]
    return ` ${day} ${time}`
}
setInterval(() => {
    time.textContent = getDate()
    time_commo.textContent = getDate()
}, 1000);

//growing line
const grow = document.querySelector(".grow_line")
const growingLine = new Chart(grow, {
    type: 'line',
    data: {
        
        labels: productArr,
        datasets: [{
            borderColor: Utils.CHART_COLORS.red,
            borderWidth: 1,
            radius: 0,
            data: data,
          },
          {
            borderColor: Utils.CHART_COLORS.blue,
            borderWidth: 1,
            radius: 0,
            data: data2,
          }]
    },
    options: {
        animation,
        interaction: {
          intersect: false
        },
        plugins: {
          legend: false
        },
        scales: {
          x: {
            type: 'linear'
          }
        }
      }
});