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

<div>This site is just the project for CSCI 6314.</div>