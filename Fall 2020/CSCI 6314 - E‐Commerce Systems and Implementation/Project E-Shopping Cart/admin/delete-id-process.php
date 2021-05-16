<?php
   require_once '../scripts/databaseConnection/db_connect.php';

session_start();
if (is_null($_SESSION['loggedin'])) {
   header('Location: index.php');
   exit;
}

$id = $mysqli->real_escape_string($_GET["delete_id"]);

$sql = "DELETE FROM items WHERE id='$id'";
if ($mysqli->query($sql)) {
    print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");
} else {
    echo "Error deleting record: " . $mysqli->connect_errno;
}
$mysqli->close();
?>
