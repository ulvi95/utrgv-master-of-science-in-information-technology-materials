<html>
    <!--https://phppot.com/php/creating-dynamic-data-graph-using-php-and-chart-js/-->
    <div id="charts">
        <canvas id="chart2"></canvas>
    </div>
    <script src='https://cdn.jsdelivr.net/npm/chart.js@2.8.0'></script>
    <script src='jquery.js'></script>
    <script>  
        $(document).ready(function (){
            showGraph();
        });
    
        function showGraph(){
            {
                $.post('data2.php',
                function(data){
                    console.log(data);
                    data=JSON.parse(data);
                    var devID=[];
                    var deviceStat=[];
                
                    for (var i in data){
                        devID.push(data[i].DevID);
                        deviceStat.push(data[i].DeviceStatus);
                    }
                
                    var chartdata={
                        labels: devID,
                        datasets:[{
                            label: 'Switch Statuses',
                            borderColor: '#F778A1',
                            data: deviceStat
                        }]
                    };
                    var graphTarget = $("#chart2");
            
                    var linegraph = new Chart (graphTarget,{
                        type: 'bar',
                        data: chartdata,
                        options:{
                            scales:{
                                xAxes:[{
                                    scaleLabel:{
                                        display: true,
                                        fontColor:'#6C2DC7',
                                        labelString: 'Switch name'
                                        
                                    },
                                    ticks: {
                                        fontColor:'#6C2DC7'
                                    }
                                }],
                                yAxes:[{
                                    scaleLabel:{
                                        display: true,
                                        fontColor:'#6C2DC7',
                                        labelString: 'Switch Status (0 or 1)'
                                    },
                                    ticks: {
                                        fontColor:'#6C2DC7',
                                        suggestedMin:0,
                                        stepSize:1,
                                        suggestedMax:1
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