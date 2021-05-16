<html>
    <!--https://phppot.com/php/creating-dynamic-data-graph-using-php-and-chart-js/-->
    <div id="charts">
        <canvas id="chart1"></canvas>
    </div>
    <script src='https://cdn.jsdelivr.net/npm/chart.js@2.8.0'></script>
    <script src='jquery.js'></script>
    <script>  
        $(document).ready(function (){
            showGraph();
        });
    
        function showGraph(){
            {
                $.post('data.php',
                function(data){
                    console.log(data);
                    data=JSON.parse(data);
                    var time=[];
                    var mid=[];
                
                    for (var i in data){
                        time.push(data[i].TimestampInfo);
                        mid.push(data[i].MessageID);
                    }
                
                    var chartdata={
                        labels: time,
                        datasets:[{
                            label: 'LED Monitoring',
                            borderColor: '#F778A1',
                            data: mid
                        }]
                    };
                    var graphTarget = $("#chart1");
            
                    var linegraph = new Chart (graphTarget,{
                        type: 'bar',
                        data: chartdata,
                        options:{
                            scales:{
                                xAxes:[{
                                    scaleLabel:{
                                        display: true,
                                        fontColor:'#6C2DC7',
                                        labelString: 'Time Stamp'
                                    },
                                    ticks: {
                                        fontColor:'#6C2DC7'
                                    }
                                }],
                                yAxes:[{
                                    scaleLabel:{
                                        display: true,
                                        fontColor:'#6C2DC7',
                                        labelString: 'MessageID'
                                    },
                                    ticks: {
                                        fontColor:'#6C2DC7',
                                        suggestedMin:12,
                                        suggestedMax:15
                                    }
                                }]
                            }
                        }
                    });
                });
            
            }
        }
    </script>
</html>