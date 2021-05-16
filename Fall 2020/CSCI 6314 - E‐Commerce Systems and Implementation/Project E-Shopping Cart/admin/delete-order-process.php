<?php
   require_once '../scripts/databaseConnection/db_connect.php';

session_start();
if (is_null($_SESSION['loggedin'])) {
   header('Location: index.php');
   exit;
}

$value = $_GET["delete_order_name"];

$sql = "DELETE FROM orders WHERE order_id='$value'";
if ($mysqli->query($sql)) {
    header("refresh:1; url=adminPage.php");
} else {
    echo "Error deleting record: " . $mysqli->connect_errno;
}
$mysqli->close();
?>
