<?php
   require_once '../scripts/databaseConnection/db_connect.php';

if(isset($_POST['submitButtonforItems']) && $_POST['submitButtonforItems'])
{

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
$activation_status = 'yes';
$item_count = $_POST['ItemCounter'];
$file_tmp_path = $_FILES['ItemPicturePath']['tmp_name'];
$id;

if ($item_count == 0)
{
	$activation_status = 'no';
}

move_uploaded_file($file_tmp_path, $filestore);

if ($stmt = $mysqli->prepare("INSERT INTO items (name, description, price, filepath, activation_status, item_count) VALUES (?, ?, ?, ?, ?, ?)"))
{
$stmt->bind_param("ssdssi", $name, $description, $price, $filepath, $activation_status, $item_count);
$stmt->execute();
$id = $mysqli->insert_id;
}

if ($stmt = $mysqli->prepare("INSERT INTO items_and_categories (id, category) VALUES (?, ?)"))
{
$stmt->bind_param("is", $id, $category);
$stmt->execute();
}

$mysqli->close();
print("<script type=\"text/javascript\">location.href=\"adminPage.php\"</script>");

}

?>