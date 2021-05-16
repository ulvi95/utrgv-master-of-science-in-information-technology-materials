<?php

session_start();

if (isset($_POST['AddToCart']))
{


if(empty($_SESSION['cart_to_sell']))
{
$_SESSION['cart_to_sell']['ProductID'] = [];
$_SESSION['cart_to_sell']['ProductImage'] = [];
$_SESSION['cart_to_sell']['ProductPrice'] = [];
$_SESSION['cart_to_sell']['ProductQuantity'] = [];
$_SESSION['cart_to_sell']['ProductPriceAndQuantity'] = [];
}

$product_id = $_POST['ProductID'];
$product_price = $_POST['ProductPrice'];
$product_quantity = $_POST['ProductQuantity'];
$product_image = $_POST['ProductImage'];

if(empty($_SESSION['cart_to_sell']['ProductID']))
{
$_SESSION['cart_to_sell']['ProductID'][] = $product_id;
$_SESSION['cart_to_sell']['ProductImage'][] = $product_image;
$_SESSION['cart_to_sell']['ProductQuantity'][] = $product_quantity;
$_SESSION['cart_to_sell']['ProductPrice'][] = $product_price;
$_SESSION['cart_to_sell']['ProductPriceAndQuantity'][] = $product_price*$product_quantity;
$_SESSION['cart_to_sell']['CartCount']++;
$_SESSION['cart_to_sell']['CartTotal'] += $product_price*$product_quantity;
print("<script type=\"text/javascript\">location.href=\"index.php\"</script>");
}

else if(!in_array($_POST['ProductID'], $_SESSION['cart_to_sell']['ProductID']))
{
$_SESSION['cart_to_sell']['ProductID'][] = $product_id;
$_SESSION['cart_to_sell']['ProductImage'][] = $product_image;
$_SESSION['cart_to_sell']['ProductQuantity'][] = $product_quantity;
$_SESSION['cart_to_sell']['ProductPrice'][] = $product_price;
$_SESSION['cart_to_sell']['ProductPriceAndQuantity'][] = $product_price*$product_quantity;
$_SESSION['cart_to_sell']['CartCount']++;
$_SESSION['cart_to_sell']['CartTotal'] += $product_price*$product_quantity;
print("<script type=\"text/javascript\">location.href=\"index.php\"</script>");
}
else
{
  print("<script>alert(\"The product is in the cart already!\")</script>");
  print("<script type=\"text/javascript\">location.href=\"index.php\"</script>");
}

}
?>