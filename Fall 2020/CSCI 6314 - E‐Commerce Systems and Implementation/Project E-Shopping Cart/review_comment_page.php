<?php
   require_once 'scripts/databaseConnection/db_connect.php';

session_start();
if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);
}

$id = $mysqli->real_escape_string($_GET["comment_id"]);

?>
<html lang="en">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="styles2.css">
      <script src="/scripts/jquery/jquery-3.5.1.min.js"></script>
      <script src="/scripts/bootstrap/js/bootstrap.bundle.min.js"></script>
      <link rel="stylesheet" href="/scripts/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/all.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/font-awesome.min.css">
      <title>CSCI 6314 E-Shopping Cart</title>
   </head>
   <body>
   <table border="1">
   <?php
   $result = $mysqli->query("SELECT * FROM comments WHERE id=$id");
   if ($result->num_rows > 0)
   {
   while($row = $result->fetch_array(MYSQLI_BOTH)) {
   ?>
   <tr><td align="center">Commentator Name</td><td align="center"><?php echo htmlentities($row['commentator_name']); ?></td></tr>
   <tr><td align="center">Comment</td><td align="center"><?php echo htmlentities($row['comment_text']); ?></td></tr>
   <tr><td align="center">Rating</td><td align="center"><?php echo htmlentities($row['rating']); ?></td></tr>
   <th><div></div><div></div></th>
   <th><div></div><div></div></th>
   <?php
   }
   }
   else
   {
   	echo "There is no comment";
   }
   ?>
</table>
<br><br><a href="index.php">Go back to the main page.</a>
    </body>
</html>