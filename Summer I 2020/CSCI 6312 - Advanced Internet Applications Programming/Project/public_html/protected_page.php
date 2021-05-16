<?php
require_once __DIR__ . '/../required/db_connect.php';
require_once __DIR__ . '/../required/functions.php';
secure_session_start();
?>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Protected Page</title>
</head>
<body>
Welcome to Jane Doe’s Clients Main Page </br>
======================================= </br>
<?php if (login_check($mysqli)) : ?>
<p>Welcome <?php echo htmlentities($_SESSION['username']); ?>!</p>
<?php
// Echo out the data in the database.
if ($stmt=$mysqli->prepare("SELECT * FROM person LIMIT 100")) {
$stmt->execute();
$stmt->bind_result($pname,$street,$city);
printf("Name Street City</br>");
while ($stmt->fetch()) {
echo $pname . " " . $street . " " . $city . "</br>";
}
$stmt->close();
}
else{ echo "error";}
$mysqli->close();
?>
<form action='scripts/process_logout.php' method="post">
<input type="submit" value='Logout' />
</form>
<?php else : ?>
<p>
<span class="error">Not authorized to access this page.</span> Please <ahref="index.php">login</a>.
</p>
<?php endif; ?>
========================================</br>
</body>
</html>