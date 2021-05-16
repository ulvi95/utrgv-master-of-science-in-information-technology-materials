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

<div class="form-group">
<form action="add_comment_process.php" method="post" enctype="multipart/form-data">
<input type="hidden" class="form-control" id="<?php echo $id ?>" name="ItemID" value="<?php echo $id ?>" aria-describedby="itemid">
<label for="ItemName">Commentator name</label>
<input type="text" class="form-control" id="CommentatorName" name="CommentatorName" aria-describedby="commentatorname" placeholder="Enter your name. No more than 255 symbols" required="required">
<label for="ItemDescription">Comment</label>
<textarea class="form-control" id="CommentText" name="CommentText" aria-describedby="commenttext" placeholder="Enter the comments. No more than 1023 symbols" rows="4" cols="50" maxlength="1024"  required="required"></textarea>
<label for="ItemPrice">Enter the rating</label>
<input type="number" class="form-control" id="Rating" name="Rating" aria-describedby="rating" placeholder="Enter the price" min="1" max="5" step="1" value="5">
<input type="submit" id="submitButtonforComments" name="submitButtonforComments" value="Submit the comment" class="btn btn-primary">
</form>
<br><br><a href="index.php">Go back to the main page.</a>
</div>
</body>
</html>

