<?php
require_once __DIR__ . '/scripts/databaseConnection/db_connect.php';
$username = "ulvi";
$password = "testpassword"; //set this to ****** when done so the script does not show the password
$email = "ulvi@test.com";
if ($stmt = $mysqli->prepare("INSERT INTO users (username, password, email) VALUES (?, ?, ?)")) {
$hashedPassword = password_hash($password, PASSWORD_DEFAULT);
$stmt->bind_param('sss',$username, $hashedPassword, $email); //'sss': each s corresponds to the type of param
$stmt->execute(); //First & 2nd params are string type
}
?>