$(function () {

  'use strict'
  $("#example1").DataTable({
      "responsive": true,
      "autoWidth": false,
      "searching": false,
    })
  //Date range picker
  $('#reservation').daterangepicker({
      singleDatePicker: true,
      startDate: moment(),
      locale: {
        format: 'YYYY-MM-DD'
      }
    },
  )

  var ticksStyle = {
    fontColor: '#495057',
    fontStyle: 'bold'
  }

  var mode      = 'index'
  var intersect = true
  //var ctx = document.getElementById('visitors-chart').getContext('2d');

  var $visitorsChart = $('#visitors-chart')
  var s1Chart  = new Chart($visitorsChart, {
    type  : 'line',
    data   : {
      labels : s1label,
      datasets: [{
        data                : s1data,
        backgroundColor     : 'transparent',
        borderColor         : '#007bff',
        pointBorderColor    : '#007bff',
        pointBackgroundColor: '#007bff',
        fill                : false,
        steppedLine: false,
      }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },

      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            stepSize:1,
            suggestedMax: 1
          }, ticksStyle)
        }],

        xAxes: [{
          type: 'time',
          time: {
            min: moment(),
            max: moment().add(12,'hours'),
            unit: 'hour',
            unitStepSize: 0.5,
            tooltipFormat: 'h:mm:ss a',
            displayFormats:{
              hour: 'MMM D, h:mm A'
            },
          },
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })

  var $s2Chart = $('#s2-chart')
  var s2Chart  = new Chart($s2Chart, {
    type  : 'line',
    data   : {
      labels : s2label,
      datasets: [{
        data                : s2data,
        backgroundColor     : 'transparent',
        borderColor         : '#007bff',
        pointBorderColor    : '#007bff',
        pointBackgroundColor: '#007bff',
        fill                : false,
        steppedLine: false,
      }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },

      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            stepSize:1,
            suggestedMax: 1
          }, ticksStyle)
        }],

        xAxes: [{
          type: 'time',
          time: {
            min: moment(),
            max: moment().add(12,'hours'),
            unit: 'hour',
            unitStepSize: 0.5,
            tooltipFormat: 'h:mm:ss a',
            displayFormats:{
              hour: 'MMM D, h:mm A'
            },
          },
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })

  var $s3Chart = $('#s3-chart')
  var s3Chart  = new Chart($s3Chart, {
    type  : 'line',
    data   : {
      labels : s3label,
      datasets: [{
        data                : s3data,
        backgroundColor     : 'transparent',
        borderColor         : '#007bff',
        pointBorderColor    : '#007bff',
        pointBackgroundColor: '#007bff',
        fill                : false,
        steppedLine: false,
      }]
    },
    options: {
      maintainAspectRatio: false,
      tooltips           : {
        mode     : mode,
        intersect: intersect
      },
      hover              : {
        mode     : mode,
        intersect: intersect
      },
      legend             : {
        display: false
      },

      scales             : {
        yAxes: [{
          // display: false,
          gridLines: {
            display      : true,
            lineWidth    : '4px',
            color        : 'rgba(0, 0, 0, .2)',
            zeroLineColor: 'transparent'
          },
          ticks    : $.extend({
            beginAtZero : true,
            stepSize:1,
            suggestedMax: 1
          }, ticksStyle)
        }],

        xAxes: [{
          type: 'time',
          time: {
            min: moment(),
            max: moment().add(12,'hours'),
            unit: 'hour',
            unitStepSize: 0.5,
            tooltipFormat: 'h:mm:ss a',
            displayFormats:{
              hour: 'MMM D, h:mm A'
            },
          },
          display  : true,
          gridLines: {
            display: true
          },
          ticks    : ticksStyle
        }]
      }
    }
  })


  $(".btn").click(function(){
    var AMPM = $("#AMPM_Selector").val();
    var DATE = $("#reservation").val();
    var CHART_DATA = s1Chart.config.options;
    var S2_CHART_DATA = s2Chart.config.options;
    var S3_CHART_DATA = s3Chart.config.options;

    if(AMPM === "AM"){
      var start_DateTime = moment(DATE + ' 08:00:00')
      var end_DateTime = moment(start_DateTime).add(12,'hours')
    } else if (AMPM === "PM"){
      var start_DateTime = moment(DATE + ' 20:00:00')
      var end_DateTime = moment(start_DateTime).add(12,'hours')
    }

    CHART_DATA.scales.xAxes[0].time.min = start_DateTime;
    CHART_DATA.scales.xAxes[0].time.max = end_DateTime;
    S2_CHART_DATA.scales.xAxes[0].time.min = start_DateTime;
    S2_CHART_DATA.scales.xAxes[0].time.max = end_DateTime;
    S3_CHART_DATA.scales.xAxes[0].time.min = start_DateTime;
    S3_CHART_DATA.scales.xAxes[0].time.max = end_DateTime;

    s1Chart.update();
    s2Chart.update();
    s3Chart.update();
    //alert(console.log(CHART_DATA.scales.xAxes[0].time.min))
    //alert(console.log(end_DateTime))
  })


})
