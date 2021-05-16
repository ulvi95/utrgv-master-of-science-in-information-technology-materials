<?php
require_once __DIR__ . '/../required/db_connect.php';
$username = "ben";
$password = "benpass"; //set this to ****** when done so the script does not show the password
if ($stmt = $mysqli->prepare("INSERT INTO webuser (pname, password) VALUES (?, ?)")) {
$hashedPassword = password_hash($password, PASSWORD_DEFAULT);
$stmt->bind_param('ss',$username, $hashedPassword); //'ss': each s corresponds to the type of param
$stmt->execute(); //First & 2nd params are string type
}
?>