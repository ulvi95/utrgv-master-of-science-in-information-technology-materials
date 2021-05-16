<?php
require_once __DIR__ . '/../../required/functions.php'; // point to the support functions created earlier
secure_session_start();
$_SESSION = array(); // set session data to an empty array… destroy the session data
$params = session_get_cookie_params();
// Set cookie's time to the past to expire it
setcookie(session_name(), ' ', time() - 42000, $params["path"], $params["domain"], $params["secure"], $params["httponly"]);
session_destroy();
header('Location: ../../index.php'); // after destroying the session reroute to the public facing page
?>