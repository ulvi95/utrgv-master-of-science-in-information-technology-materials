<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "colors";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

?>

<html>
<head>
<title>
Database Test
</title>
</head>
<body>
<form method="post" action="" name="ColorTest">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name"><br><br>
<label for="colors1">First Favorite Color:</label>
<select name="colors1" id="colors1">
  <option value="green">Green</option>
  <option value="blue">Blue</option>
  <option value="red">Red</option>
  <option value="yellow">Yellow</option>
  <option value="black">Black</option>
</select>
<br><br>
<label for="colors2">Second Favorite Color:</label>
<select name="colors2" id="colors2">
  <option value="green">Green</option>
  <option value="blue">Blue</option>
  <option value="red">Red</option>
  <option value="yellow">Yellow</option>
  <option value="black">Black</option>
</select>
<br><br>
<label for="colors3">Third Favorite Color:</label>
<select name="colors3" id="colors3">
  <option value="green">Green</option>
  <option value="blue">Blue</option>
  <option value="red">Red</option>
  <option value="yellow">Yellow</option>
  <option value="black">Black</option>
</select>
<br><br>
<label for="colors4">Fourth Favorite Color:</label>
<select name="colors4" id="colors4">
  <option value="green">Green</option>
  <option value="blue">Blue</option>
  <option value="red">Red</option>
  <option value="yellow">Yellow</option>
  <option value="black">Black</option>
</select>
<br><br>
<label for="colors5">Fifth Favorite Color:</label>
<select name="colors5" id="colors5">
  <option value="green">Green</option>
  <option value="blue">Blue</option>
  <option value="red">Red</option>
  <option value="yellow">Yellow</option>
  <option value="black">Black</option>
</select>
<br><br>
<input type="submit" value="Submit">
</form>
<?php
$sql = "SELECT Name, FavColor FROM colors";
$result = $conn->query($sql);

if ($result->num_rows > 0)
{
  // output data of each row
  while($row = $result->fetch_assoc())
  {
    echo "name: " . $row["Name"]. " Color: " . $row["FavColor"] . "<br>";
  }
}
else
{
echo "no data yet";
}

?>

<?php

if (isset($_POST['name']) && !empty($_POST['name']))
{

$name = $_POST['name'];
$first = $_POST['colors1'];
$second = $_POST['colors2'];
$third = $_POST['colors3'];
$fourth = $_POST['colors4'];
$fifth = $_POST['colors5'];


$sql = "INSERT INTO colors (Name, FavColor) VALUES ('$name', '$first');";
$sql .= "INSERT INTO colors (Name, FavColor) VALUES ('$name', '$second');";
$sql .= "INSERT INTO colors (Name, FavColor) VALUES ('$name', '$third');";
$sql .= "INSERT INTO colors (Name, FavColor) VALUES ('$name', '$fourth');";
$sql .= "INSERT INTO colors (Name, FavColor) VALUES ('$name', '$fifth');";

if ($conn->multi_query($sql) === TRUE) {
  echo "New records created successfully";
  $_POST['name'] = "";
} else {
  echo "Error: " . $sql . "<br>" . $conn->error;
}
$conn->close();
}
else
{

}
?>




</body>
</html>


