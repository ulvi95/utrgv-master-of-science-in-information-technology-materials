<?php
   require_once 'scripts/databaseConnection/db_connect.php';

session_start();
if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);
}

if(empty($_SESSION['cart_to_sell']))
{
  $_SESSION['cart_to_sell'] = [];
  $_SESSION['cart_to_sell']['CartCount'] = 0;
  $_SESSION['cart_to_sell']['CartTotal'] = 0.00;
}

?>

<html lang="en">
<head>
	<!-- Required meta tags -->
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
	<link rel="stylesheet" href="styles.css">
	<link rel="stylesheet" href="scripts/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="scripts/fontawesome/css/all.min.css">
	<link rel="stylesheet" href="scripts/fontawesome/css/font-awesome.min.css">


<title>CSCI 6314 E-Shopping Cart</title>
</head>
<body>


<div class="container" id="headerForIndex">
	<div class="row" id="headerRow">
		<h1 id="headerRowText">Welcome to the CSCI 6314 Project E-Commerse Shopping Cart!</h1>
	</div>
</div>
<nav class="navbar navbar-dark navbar-expand-lg" id="top">
  <div class="container-fluid">
    <ul class="nav navbar-nav left">
      <li class="active"><a href="index.php">Home</a></li>
      <li><a href="category-search-page.php">Catalog by Categories</a></li>
      <li><a href="mailto:ulvi.bajarani01@utrgv.edu">Contact Us</a></li>
      <li><a href="about.php">About</a></li>
      <li><a href="cart.php"><i class="fas fa-shopping-cart"></i> Shopping <?php echo $_SESSION['cart_to_sell']['CartCount'] ?> items in your cart | Total <?php echo $_SESSION['cart_to_sell']['CartTotal'] ?> USD</a></li>
      <li><a href="clean-cart.php"><i class="fas fa-ban"></i> Clean Cart</a></li>
  </div>
</nav>


<div id="Products">
<div class="row">
<?php
$result = $mysqli->query("SELECT * FROM items WHERE activation_status = 'yes' AND item_count > 0");

if($result->num_rows > 0)
{
while($row = $result->fetch_array(MYSQLI_BOTH))
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
?>
</div>
</div>


<script src="scripts/jquery/jquery-3.5.1.min.js"></script>
<script src="scripts/bootstrap/js/bootstrap.bundle.min.js"></script>


</body>
</html>