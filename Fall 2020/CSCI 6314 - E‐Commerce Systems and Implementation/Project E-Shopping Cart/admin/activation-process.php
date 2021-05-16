<?php
   require_once '../scripts/databaseConnection/db_connect.php';

session_start();
if (is_null($_SESSION['loggedin'])) {
   header('Location: index.php');
   exit;
}

$id = $mysqli->real_escape_string($_GET["activate_id"]);

$result = $mysqli->query("SELECT activation_status FROM items WHERE id='$id'");
if($result->num_rows > 0){
while($row = $result->fetch_array(MYSQLI_BOTH))
{
if($row["activation_status"] == 'yes')
{
$mysqli->query("UPDATE items SET activation_status='no' WHERE id='$id'");
}
else if($row["activation_status"] == 'no')
{
$mysqli->query("UPDATE items SET activation_status='yes' WHERE id='$id'");
}
}
}

print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");

?>