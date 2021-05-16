<?php
   require_once '../scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforCategoryEditor']) && $_POST['submitButtonforCategoryEditor'])
{

$category_old = $_POST['ItemCategoryOldName'];
$category_new = $_POST['ItemCategoryNewName'];

$sql = "UPDATE categories set category='$category_new' WHERE category='$category_old'";

$mysqli->query($sql);

$mysqli->close();

print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");
}



?>