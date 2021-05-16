<?php
   require_once '../scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforCategories']) && $_POST['submitButtonforCategories'])
{

$id = $_POST['ItemID'];
$category = $_POST['ItemCategory'];

if ($stmt = $mysqli->prepare("INSERT INTO items_and_categories (id, category) VALUES (?, ?)"))
{
$stmt->bind_param("is", $id, $category);
$stmt->execute();
}

$mysqli->close();
print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");

}

?>