<?php
   require_once '../scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforItems']) && $_POST['submitButtonforItems'])
{

$id = $_POST['ItemID'];
$name = $_POST['ItemName'];
$description = $_POST['ItemDescription'];
$price = $_POST['ItemPrice'];
$category = $_POST['ItemCategory'];
$filepath;
if(isset($_FILES['ItemPicturePath']['name']) && $_FILES['ItemPicturePath']['name'])
{
$filepath = uniqid() . "_" . $_FILES['ItemPicturePath']['name'];
}
else
{
$filepath = "";
}
$filestore = "../images/".$filepath;
$activation_status = $_POST['ItemActivationStatus'];
$item_count = $_POST['ItemCounter'];
$file_tmp_path = $_FILES['ItemPicturePath']['tmp_name'];



if ($item_count == 0)
{
   $activation_status = 'no';
}

move_uploaded_file($file_tmp_path, $filestore);


$sql = "UPDATE items SET name='$name', description='$description', price='$price', filepath='$filepath', activation_status='$activation_status', item_count='$item_count' WHERE id='$id'";

$mysqli->query($sql);

if ($stmt = $mysqli->prepare("INSERT INTO items_and_categories (id, category) VALUES (?, ?)"))
{
$stmt->bind_param("is", $id, $category);
$stmt->execute();
}

$mysqli->close();
print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");

}

?>