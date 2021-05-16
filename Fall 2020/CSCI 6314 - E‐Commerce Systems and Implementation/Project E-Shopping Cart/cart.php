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
      <li><a href="cart.php"><i class="fas fa-shopping-cart"></i>Shopping <?php echo $_SESSION['cart_to_sell']['CartCount'] ?> items in your cart | Total <?php echo $_SESSION['cart_to_sell']['CartTotal'] ?> USD</a></li>
  </div>
</nav>

<div id="table">

<?php 

if(empty($_SESSION['cart_to_sell']['ProductID']))
{
echo "No item on the cart yet!";
$_SESSION['cart_to_sell']['CartCount'] = 0;
$_SESSION['cart_to_sell']['CartTotal'] = 0.00;
}
else
{
$all_id = 0;
echo "<table><th align=\"center\">Product ID</th><th align=\"center\">Product Image</th><th align=\"center\">Product Quantity</th><th align=\"center\">Product Price</th><th align=\"center\">Product Price and Quantity</th><th align=\"center\">Remove the Item from the Cart</th>";

for ($i=0; $i<count($_SESSION['cart_to_sell']['ProductID']); $i++)
{
$all_id+=$_SESSION['cart_to_sell']['ProductID'][$i];
	echo "<tr><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductID'][$i] . "</td><td align=\"center\">" . "<img class=\"card-img-top\" alt=\"Item Image\" height=\"50px\" width=\"50px\" src=\"" . $_SESSION['cart_to_sell']['ProductImage'][$i] . "\">" . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductQuantity'][$i] . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductPrice'][$i] . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductPriceAndQuantity'][$i] . "</td>"  . "<td align=\"center\">" . "<a href=\"remove-from-cart.php?remove_cart_product_id=" . $i . " \">" . "<i class=\"fas fa-ban\" title=\"Remove Item from the cart\"></i></a></td>" . "</tr>";
	
}
echo "</table>";
echo "<b>Total is </b>" . $_SESSION['cart_to_sell']['CartTotal'] . "<br>";
echo "<b>Number of items in cart is </b>" . $_SESSION['cart_to_sell']['CartCount'] . "<br>";
echo "<a class=\"btn btn-danger\" href=\"clean-cart.php\">Clean the Cart!</a>";

echo "<form class=\"paypal\" action=\"\scripts\paypalPayment\payments.php\" method=\"post\" id=\"paypal_form\">
        <input type=\"hidden\" name=\"cmd\" value=\"_xclick\" />
        <input type=\"hidden\" name=\"no_note\" value=\"1\" />
        <input type=\"hidden\" name=\"lc\" value=\"UK\" />
        <input type=\"hidden\" name=\"bn\" value=\"PP-BuyNowBF:btn_buynow_LG.gif:NonHostedGuest\" />
        <input type=\"hidden\" name=\"first_name\" value=\"Customer's First Name\" />
        <input type=\"hidden\" name=\"last_name\" value=\"Customer's Last Name\" />
        <input type=\"hidden\" name=\"payer_email\" value=\"customer@example.com\" />
        <input type=\"hidden\" name=\"item_number\" value=\"$all_id\" / >
        <input type=\"submit\" name=\"submit\" value=\"Buy now!\" class=\"btn btn-warning\"/>
    </form>";

}

?>


</div>
</table>
</div>

