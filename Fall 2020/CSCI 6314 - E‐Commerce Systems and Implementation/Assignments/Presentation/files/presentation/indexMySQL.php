<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0032;}
</style>
</head>
<body>

<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>

<?php

function data_changer($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (!(empty($_POST["name"]))) {
    $name = data_changer($_POST["name"]);
  } else {
    $nameErr = "Name is required";
  }
  
  if (!(empty($_POST["email"]))) {
    $email = data_changer($_POST["email"]);
  } else {
    $emailErr = "Email is required";
  }
    
  if (!(empty($_POST["website"]))) {
    $website = data_changer($_POST["website"]);
  } 

  if (!(empty($_POST["comment"]))) {
    $comment = data_changer($_POST["comment"]);
  }

  if (!(empty($_POST["gender"]))) {
  	$gender = data_changer($_POST["gender"]);
  } else {
    $genderErr = "Gender is required";
  }
}


?>

<h2>PHP Form Mail Preparer and Printer</h2>
<p><span class="error">* defines the required field</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  Name: <input type="text" name="name">
  <span class="error">* <?php echo $nameErr;?></span>
  <br><br>
  E-mail: <input type="text" name="email">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>
  Website: <input type="text" name="website">
  <br><br>
  Comment: <textarea name="comment" rows="6" cols="60"></textarea>
  <br><br>
  Gender:
  <input type="radio" name="gender" value="female">Female
  <input type="radio" name="gender" value="male">Male
  <input type="radio" name="gender" value="other">Other
  <span class="error">* <?php echo $genderErr;?></span>
  <br><br>
  <input type="submit" name="submit" value="Submit">  
</form>



<?php
if(isset($_POST["submit"]))
{
$sql = "INSERT INTO myguests (name, email, gender, comment, website) VALUES (?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("sssss", $name, $email, $gender, $comment, $website);
$stmt->execute();
$stmt->close();
echo "Data entered successfully!";
}
?>

</body>
</html>
