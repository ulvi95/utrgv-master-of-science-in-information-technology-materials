<?php
   require_once '../scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforCategories']) && $_POST['submitButtonforCategories'])
{

$category_adder = $_POST['CategoryAdder'];

if ($stmt = $mysqli->prepare("INSERT INTO categories (category) VALUES (?)"))
{
$stmt->bind_param("s", $category_adder);
$stmt->execute();

}
$mysqli->close();

print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");
}



?>