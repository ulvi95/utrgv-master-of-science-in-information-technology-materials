<?php
   require_once '../scripts/databaseConnection/db_connect.php';

session_start();
if (is_null($_SESSION['loggedin'])) {
   header('Location: index.php');
   exit;
}

$id = $mysqli->real_escape_string($_GET["delete_id"]);
$category = $mysqli->real_escape_string($_GET["delete_category_name"]);

$sql = "DELETE FROM items_and_categories WHERE id='$id' AND category='$category'";
if ($mysqli->query($sql)) {
    print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");
} else {
    echo "Error deleting record: " . $mysqli->connect_errno;
}
$mysqli->close();
?>
