<?php
require_once '../../scripts/databaseConnection/db_connect.php';

session_start();
if ($mysqli->connect_error)
{
    die("Connection failed: " . $mysqli->connect_error);
}

echo "<b>Items you have bought are</b><br><br><br>";
echo "<table><th align=\"center\">Product ID</th><th align=\"center\">Product Image</th><th align=\"center\">Product Quantity</th><th align=\"center\">Product Price</th><th align=\"center\">Product Price and Quantity</th>";

for ($i = 0;$i < count($_SESSION['cart_to_sell']['ProductID']);$i++)
{

    echo "<tr><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductID'][$i] . "</td><td align=\"center\">" . "<img class=\"card-img-top\" alt=\"Item Image\" height=\"50px\" width=\"50px\" src=\"../../" . $_SESSION['cart_to_sell']['ProductImage'][$i] . "\">" . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductQuantity'][$i] . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductPrice'][$i] . "</td><td align=\"center\">" . $_SESSION['cart_to_sell']['ProductPriceAndQuantity'][$i] . "</td>" . "</tr>";

}
echo "</table>";

$order_price = $_SESSION['cart_to_sell']['CartTotal'];

$order_time_result = $mysqli->query("SELECT NOW()");
$order_time_array = $order_time_result->fetch_array(MYSQLI_BOTH);
$order_time = $order_time_array[0];

$order_id;

if ($stmt = $mysqli->prepare("INSERT INTO orders (order_price, order_time) VALUES (?, ?)"))
{
    $stmt->bind_param("ds", $order_price, $order_time);
    $stmt->execute();
    $order_id = $mysqli->insert_id;
}

for ($i = 0;$i < count($_SESSION['cart_to_sell']['ProductID']);$i++)
{
    $cart_id = $_SESSION['cart_to_sell']['ProductID'][$i];
    $cart_count = $_SESSION['cart_to_sell']['ProductQuantity'][$i];
    $sql_update = "UPDATE items SET item_count = item_count - $cart_count WHERE id=$cart_id";
    $mysqli->query($sql_update);
}

$token = $_POST['stripeToken'];
$email = $_POST['stripeEmail'];
$amount = $_SESSION['cart_to_sell']['CartTotal'];

session_destroy();

echo '<h1>Successfully charged ' . $amount . ' $!</h1><br>';
echo '<h2>Your Order ID is ' . $order_id . '</h2><br>';
echo '<h2>Your Order price is ' . $order_price . ' $</h2><br>';
echo '<h2>Your Order time is ' . $order_time . '</h2><br>';
echo '<h1>Please, write/save everything somewhere to be able to claim back the product in the future!</h1><br>';
echo "<br><br><a href=\"../../../index.php\">Go back to the main page.</a>";

$mysqli->close();
?>
