<?php
   require_once 'scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforComments']) && $_POST['submitButtonforComments'])
{

$id = $_POST['ItemID'];
$commentator_name = $mysqli->real_escape_string(htmlentities($_POST['CommentatorName']));
$comment_text = $mysqli->real_escape_string(htmlentities($_POST['CommentText']));
$rating = $_POST['Rating'];

if ($stmt = $mysqli->prepare("INSERT INTO comments (id, commentator_name, comment_text, rating) VALUES (?, ?, ?, ?)"))
{
$stmt->bind_param("issi", $id, $commentator_name, $comment_text, $rating);
$stmt->execute();
}

$mysqli->close();
print("<script type=\"text/javascript\">location.href=\"index.php\"</script>");

}

?>