<?php
   require_once 'scripts/databaseConnection/db_connect.php';

session_start();
if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);
}

$category = $_GET['q'];
$sql;

if (($category != "none") && ($category != "empty"))
{
$sql = "SELECT `items`.`id`, `items`.`name`, `items`.`description`, `items`.`price`, `items`.`filepath`, `items`.`item_count` FROM items, items_and_categories, categories WHERE `items_and_categories`.`category` = '$category' AND `items_and_categories`.`id` = `items`.`id` AND `items_and_categories`.`category` = `categories`.`category` AND activation_status = 'yes' AND item_count > 0";
}
else if ($category == "none")
{
$sql = "SELECT * FROM items WHERE activation_status = 'yes' AND item_count > 0";
}
else if ($category == "empty")
{
echo "<div id=\"Products\">Choose the category to describe the items</div>";
}

if(isset($sql))
{
$result = $mysqli->query($sql);

if($result->num_rows > 0)
{
echo "<div class=\"row\">";

while ($row = $result->fetch_array(MYSQLI_BOTH))
{

?>

<form action="add-to-cart.php" method="post">
<div class="col-sm-4">
<div class="card" style="width: 18rem;">

  <br>
  <input type="hidden" id="ProductImage" name="ProductImage" value="images/<?php echo $row['filepath'] ?>"><img class="card-img-top" src="images/<?php echo $row['filepath']?>" alt="Item Image" height="150px" width="150px">
  <br>
<div class="card-body">
  
    <h5 class="card-title"><input type="hidden" id="ProductID" name="ProductID" value="<?php echo $row['id'] ?>"> <?php echo $row['name']?></h5>
  <button class="btn btn-primary btn-sm" type="button" data-toggle="collapse" data-target="#<?php echo $row['id']?>" aria-expanded="false" aria-controls="<?php echo $row['id']?>">
   Description
  </button>
  <div class="collapse" id="<?php echo $row['id']?>">
  <div class="card card-body">
    <?php echo $row['description']?>
  </div>
</div>
    <p class="card-text"><input type="hidden" id="ProductPrice" name="ProductPrice" value="<?php echo $row['price'] ?>"><?php echo "Price: " . $row['price'] . "$"?></p>
    <p class="card-text"><?php
    $id_for_query = $row['id'];
    $sql_average = "SELECT AVG(`rating`) AS avg_rating FROM `comments` WHERE id='$id_for_query'";
  $result_average = $mysqli->query($sql_average);
  $row_average = $result_average->fetch_object() ;
  echo "Rating: " . (isset($row_average->avg_rating) ? round($row_average->avg_rating, 2) : "N/A");?>
    <p class="card-text"><?php echo "Available count: " . $row['item_count']?></p>
    <input type="number" id="ProductQuantity" min="1" max="<?php echo $row['item_count'] ?>" value="1" step="1" name="ProductQuantity">
    <a class="btn btn-primary btn-sm" target='_blank' href='review_comment_page.php?comment_id=<?php echo $row['id']?>'>Review Comments</a>
    <a class="btn btn-primary btn-sm" target='_blank' href='add_comment_page.php?comment_id=<?php echo $row['id']?>'>Add Comments and Rate</a>
    <input class="btn btn-primary btn-sm" type="submit" name="AddToCart" method="post" value="Add to Cart">
  </form>
</div>
</div>
</div>
<?php
}
}
echo "</div>";
}
?>