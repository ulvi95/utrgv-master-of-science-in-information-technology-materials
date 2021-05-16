<?php
define('DB_HOST', 'localhost');
define('DB_USER', 'root');
define('DB_PASSWORD', 'root');
define('DB_DATABASE', 'forlab4');
$mysqli = new mysqli(DB_HOST, DB_USER, DB_PASSWORD, DB_DATABASE);

if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);
}
echo "Connected to <b>" . DB_DATABASE . "</b> successfully";
echo "<br><br>Let me fetch the data from <b>" . DB_DATABASE . "</b><br><br>...";

$sql = "SELECT name, surname FROM forlab4";
$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "The fetched result: Name: " . $row["name"]. " " . $row["surname"]. "<br>";
  }
} else {
  echo "<br><br>Sorry, there is no result. Let's try after inserting.<br><br>";
}

$sql2 = "INSERT INTO forlab4 (name, surname) VALUES ('Ulvi', 'Bajarani')";

if ($mysqli->query($sql2) === TRUE) {
  echo "<br><br>New record created successfully<br><br>";
} else {
  echo "Error: " . $sql2 . "<br>" . $mysqli->error;
}

$result = $mysqli->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "The fetched result: Name: " . $row["name"]. " " . $row["surname"]. "<br>";
  }
} else {
  echo "Sorry, there is no result. Let's try after inserting.";
}

?>