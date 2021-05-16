<?php
require_once __DIR__ . '/../required/db_connect.php';
?>
<html>
    <header>
        <title>Welcome</title>
        <meta charset="UTF-8"/>
    </header>
    <body>
        <div id="header">
            <h1>Welcome</h1>
        </div>
        <div id="body">
            <div id="status"></div>
            <script type="text/javascript" src="jquery.js"></script>
            <script src="https://cdn.jsdelivr.net/npm/chart.js@2.8.0"></script>
            <script type="text/javascript">      
                $(document).ready(function() {  
                    setInterval(function() {
                        $('#status').load('DBdevice.php')
                    }, 3000);
                }); 
            </script>
            <form id="form1" method="post" action="">
                <input type="hidden" id="out" value="1">
                <button type="submit">Logout</button>
            </form>
            <div id=check>
                <?php
                    if(isset($_POST['out'])){
                    $uname='ben';
                    $id='10';
                    date_default_timezone_set("America/Chicago");
                    $date=date("Y-m-d H:i:s");
                    $stmt=$mysqli->prepare("INSERT INTO TransactionalLogs(TimestampInfo,MessageID,DataInformation) VALUES(?,?,?)");
                    $stmt->bind_param('sss',$date,$id,$uname);
                    $stmt->execute();
                    $stmt->close();
                    echo "<script type='text/javascript'>alert('Logging Out')</script>";
                    echo "<script> window.location.assign('index.php');</script>";
                    }
                ?>
            </div>
            <div id="chartLink"><a href="Chart.php">The link to the Timestamp chart</div>
        </div>
    </body>
</html>