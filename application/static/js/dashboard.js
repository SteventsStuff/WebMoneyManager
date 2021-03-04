/* globals Chart:false, feather:false */

(() => {
    'use strict'
    feather.replace()

    // // Graphs
    // var ctx = document.getElementById('myChart')
    // // eslint-disable-next-line no-unused-vars
    // var myChart = new Chart(ctx, {
    //     type: 'line',
    //     data: {
    //         labels: [
    //             'Sunday',
    //             'Monday',
    //             'Tuesday',
    //             'Wednesday',
    //             'Thursday',
    //             'Friday',
    //             'Saturday'
    //         ],
    //         datasets: [{
    //             data: [
    //                 15339,
    //                 21345,
    //                 18483,
    //                 24003,
    //                 23489,
    //                 24092,
    //                 12034
    //             ],
    //             lineTension: 0,
    //             backgroundColor: 'transparent',
    //             borderColor: '#007bff',
    //             borderWidth: 4,
    //             pointBackgroundColor: '#007bff'
    //         }]
    //     },
    //     options: {
    //         scales: {
    //             yAxes: [{
    //                 ticks: {
    //                     beginAtZero: false
    //                 }
    //             }]
    //         },
    //         legend: {
    //             display: false
    //         }
    //     }
    // })
})()


const sideMenuTrigger = document.querySelector('#sideMenuTrigger');


sideMenuTrigger.addEventListener('click', () => {
    let row = document.getElementById('row');
    let sidebarMenu = document.getElementById('sidebarMenu');
    let sidebarMenuX = sidebarMenu.getBoundingClientRect().x;
    let sidebarMenuWidth = sidebarMenu.getBoundingClientRect().width;

    let offset = sidebarMenuWidth + 80;
    let sidebarMenuWidthWidthPx = offset.toString() + "px";

    if (sidebarMenuX < 0) {
        row.style.marginLeft = "0";
        sidebarMenu.style.marginLeft = "0";
    } else {
        row.style.marginLeft = "-" + sidebarMenuWidthWidthPx;
        sidebarMenu.style.marginLeft = "-" + sidebarMenuWidthWidthPx;
    }
})
