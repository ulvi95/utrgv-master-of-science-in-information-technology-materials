<?php
require_once __DIR__ . '/../../required/db_connect.php';
require_once __DIR__ . '/../../required/functions.php'; // point to the support functions created earlier
secure_session_start();
if (isset($_POST['username'], $_POST['password'])) { // check if values are non null
$username = $_POST['username'];
$password = $_POST['password'];
if (login($username, $password, $mysqli)) {
header('Location: ../../protected_page.php'); // access the protected page if credentials are good
} else {
header('Location: ../../index.php?error=1'); // access the public page if credentials fail
}
} else {echo 'Invalid Request… null values';}
?>