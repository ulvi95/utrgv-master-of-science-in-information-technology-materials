<?php
require_once __DIR__ . '/../required/db_connect.php'; 
?> 
<?php 
date_default_timezone_set("America/Chicago");
echo "Last update: " . date('m/d/y') . " " . date('h:i:sa') . "<br>";
echo "<h3>Status of Sensors and Acutators</h3>";
if ($stmt=$mysqli->prepare("SELECT * FROM SensorsAndActuators LIMIT 100")) {
    $stmt->execute(); 
    $stmt->bind_result($devid,$devtype,$devfun,$ctrl,$status);
    echo "<table><tr><td>Device Name</td><td>Status</td></tr>";
    while ($stmt->fetch()) {
        echo "<tr><td>$devid</td><td>$status</td></tr>";
    }
    echo "</table>";
    $stmt->close(); 
} 
else {  
    echo "error";
    $mysqli->close(); 
} 
echo "<hr>";
echo "<h3>Alarm Status</h3>";
if ($stmt=$mysqli->prepare("SELECT a1.AlarmID, a1.SinceTS, a1.AcknowledgementStatus,c1.MessageDescription FROM ActiveAlarms a1 LEFT JOIN Alarms a2 ON a1.AlarmID=a2.AlarmID LEFT JOIN CannedMessages c1 ON a2.MessageID=c1.MessageID")) {
    $stmt->execute(); 
    $stmt->bind_result($alarmid,$since,$acknowl,$description);
    echo "<table><tr><td>Alarm</td><td>Description</td><td>Since</td><td>Acknowledged</td></tr>";
    while ($stmt->fetch()) {
        if ($acknowl!=1){
            echo "<tr><td>$alarmid</td><td>$description</td><td>$since</td><td>$acknowl</td></tr>";
        }
    }
    echo "</table>";
    $stmt->close(); 
} 
else {  
    echo "error";
    $mysqli->close(); 
} 
echo "<hr>";
?>