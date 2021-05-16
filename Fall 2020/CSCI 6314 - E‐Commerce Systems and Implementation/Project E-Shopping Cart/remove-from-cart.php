<?php
session_start();

$remove_id = $_GET["remove_cart_product_id"];

if(!empty($_SESSION['cart_to_sell']) && in_array($_SESSION['cart_to_sell']['ProductID'][$remove_id], $_SESSION['cart_to_sell']['ProductID']))
{	
	unset($_SESSION['cart_to_sell']['ProductID'][$remove_id]);
	unset($_SESSION['cart_to_sell']['ProductImage'][$remove_id]);
	unset($_SESSION['cart_to_sell']['ProductPrice'][$remove_id]);
	unset($_SESSION['cart_to_sell']['ProductQuantity'][$remove_id]);
	$_SESSION['cart_to_sell']['CartCount']--;
	$_SESSION['cart_to_sell']['CartTotal'] -= $_SESSION['cart_to_sell']['ProductPriceAndQuantity'][$remove_id];
	unset($_SESSION['cart_to_sell']['ProductPriceAndQuantity'][$remove_id]);
	if(!empty($_SESSION['cart_to_sell']))
	{
	$_SESSION['cart_to_sell']['ProductID'] = array_values($_SESSION['cart_to_sell']['ProductID']);
	$_SESSION['cart_to_sell']['ProductImage'] = array_values($_SESSION['cart_to_sell']['ProductImage']);
	$_SESSION['cart_to_sell']['ProductPrice'] = array_values($_SESSION['cart_to_sell']['ProductPrice']);
	$_SESSION['cart_to_sell']['ProductQuantity'] = array_values($_SESSION['cart_to_sell']['ProductQuantity']);
	$_SESSION['cart_to_sell']['ProductPriceAndQuantity'] = array_values($_SESSION['cart_to_sell']['ProductPriceAndQuantity']);
	}
	if(empty($_SESSION['cart_to_sell']) || ($_SESSION['cart_to_sell']['CartTotal'] < 0) || ($_SESSION['cart_to_sell']['CartCount'] <= 0))
	{
	$_SESSION['cart_to_sell']['CartCount'] = 0;
	$_SESSION['cart_to_sell']['CartTotal'] = 0.00;
	}

	print("<script type=\"text/javascript\">alert(\"The product is removed from the cart successfully!\")</script>");
    print("<script type=\"text/javascript\">location.href=\"cart.php\"</script>");
}
else
{	
	print("<script type=\"text/javascript\">alert(\"Error: Either the item is not found or the array is empty.\")\"</script>");
    print("<script type=\"text/javascript\">location.href=\"cart.php\"</script>");
}
?>