<html>
<head>
	<title>Assignment by Ulvi Bajarani</title>
</head>
<body>
<script type="text/javascript">
	document.write("Let's try to get the data from Database by PHP (This string is written in JavaScript).<br><br>");
</script>

</body>

</html>

<?php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'root');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD);

if ($mysqli->connect_error) {
  die("connection failed: " . $mysqli->connect_error);
}
$sql = "CREATE DATABASE IF NOT EXISTS forassignment2";

if ($mysqli->query($sql) === TRUE) {
  echo "We have created the database.<br><br>";
} else {
  echo "Error creating database: " . $mysqli->error . "<br><br>";
}

$mysqli->close();

define('DB_DATABASE', 'forassignment2');

$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);

if ($mysqli->connect_error) {
  die("connection failed: " . $mysqli->connect_error);
}

$sql = "CREATE TABLE IF NOT EXISTS forassignment2(id INT(8), name VARCHAR(255))";

if ($mysqli->query($sql) === TRUE) {
  echo "We have created the table. Let's add the data.<br><br>";
} else {
  echo "Error creating table: " . $mysqli->error . "<br><br>";
}

$id = rand(1,10000);
$name = "Random number by Ulvi";
$sql2 = "INSERT INTO forassignment2 VALUES ($id, '$name')";

if ($mysqli->query($sql2) === TRUE) {
  echo "The data added successfully.<br><br>";
} else {
  echo "Error adding data: " . $mysqli->error . "<br><br>";
}

echo "Let's fetch the data from database.<br><br>";

$sql3 = "SELECT id, name FROM forassignment2";

$result = $mysqli->query($sql3);
if ($result->num_rows > 0)
{
	while ($row = $result->fetch_assoc())
	{
		echo "Random Number: " . $row["id"]. " - Name: " . $row["name"]. "<br>";
	}
}
else {
  echo "0 results";
}

echo "<br>Let's update our newly added data from database.<br><br>";
$sql4 = "UPDATE forassignment2 SET name='Just the random number' WHERE name='Random number by Ulvi'";

if ($mysqli->query($sql4) === TRUE) {
  echo "Record updated successfully<br><br>";
} else {
  echo "Error updating record: " . $mysqli->error;
}
echo "Let's fetch the data from database again. Make an attention to the last string.<br><br>";

$result = $mysqli->query($sql3);

if ($result->num_rows > 0)
{
	while ($row = $result->fetch_assoc())
	{
		echo "Random Number: " . $row["id"]. " - Name: " . $row["name"]. "<br>";
	}
}
else {
  echo "0 results";
}
$mysqli->close();

?>