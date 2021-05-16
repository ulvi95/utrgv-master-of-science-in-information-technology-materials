<?php
require_once __DIR__ . '/../required/db_connect.php'; 

$stmt = "SELECT MessageID, TimestampInfo FROM TransactionalLogs ORDER BY TimestampInfo";
$result = mysqli_query($mysqli,$stmt);
$data = array();
foreach ($result as $row){
    $data[] = $row;
}
mysqli_close($mysqli);
echo json_encode($data);
?> 