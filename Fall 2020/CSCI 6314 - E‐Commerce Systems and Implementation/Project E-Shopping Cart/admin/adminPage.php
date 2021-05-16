<?php
   require_once '../scripts/databaseConnection/db_connect.php';

session_start();
if ($mysqli->connect_error) {
  die("Connection failed: " . $mysqli->connect_error);

}

if (is_null($_SESSION['loggedin'])) {
   header('Location: index.php');
   exit;
}


?>
<html lang="en">
   <head>
      <!-- Required meta tags -->
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
      <!-- Bootstrap CSS -->
      <link rel="stylesheet" href="styles2.css">
      <script src="/scripts/jquery/jquery-3.5.1.min.js"></script>
      <script src="/scripts/bootstrap/js/bootstrap.bundle.min.js"></script>
      <link rel="stylesheet" href="/scripts/bootstrap/css/bootstrap.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/all.min.css">
      <link rel="stylesheet" href="/scripts/fontawesome/css/font-awesome.min.css">
      <title>CSCI 6314 E-Shopping Cart</title>
   </head>
   <body>
      <div class="panel-group btn btn-light btn-group-vertical justify-content-center" id="accordion">
         <div class="panel panel-default">
            <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse1">
                  Add Item</a>
               </h4>
            </div>
            <div id="collapse1" data-parent="#accordion" class="panel-collapse collapse in">
                  <div class="panel-body">
                  	<form action="item_adder.php" method="post" enctype="multipart/form-data">
                     <div class="form-group">
                        <label for="ItemName">Item Name</label>
                        <input type="text" class="form-control" id="ItemName" name="ItemName" aria-describedby="itemname" placeholder="Enter the item name. No more than 255 symbols" required="required">
                     </div>
                     <div class="form-group">
                        <label for="ItemDescription">Item Description</label>
                        <textarea class="form-control" id="ItemDescription" name="ItemDescription" aria-describedby="itemdescription" placeholder="Enter the item description. No more than 1023 symbols" rows="4" cols="50" maxlength="1024" required="required"></textarea>
                     </div>
                     <div class="form-group">
                        <label for="ItemPrice">Item Price</label>
                        <input type="number" class="form-control" id="ItemPrice" name="ItemPrice" aria-describedby="itemprice" placeholder="Enter the price" min="0" max="1000" step=".01" value="0" required="required">
                     </div>
                     <div class="form-group">
                        <label for="ItemCategory">Item Category</label>
                        <select name="ItemCategory" id="ItemCategory">
                        	<?php
						$result = $mysqli->query("SELECT * FROM categories");
                  if($result->num_rows > 0)
                     {
                  while($row = $result->fetch_array(MYSQLI_BOTH))
                  {
                        echo "<option value='".$row['category']."'>".$row['category']."</option>";
						}
                      }
                  else
                  {
                     echo "<option value='". "'>" . "</option>";
                  }
						?>
						</select>
                     </div>
                     <div class="form-group">
                        <label for="ItemPicturePath">Item Picture Path</label>
                        <input type="file" class="form-control" id="ItemPicturePath" name="ItemPicturePath" aria-describedby="ItemPicturePath" placeholder="Add the product picture">
                     </div>
                     <div class="form-group">
                        <label for="ItemCounter">Item Count</label>
                        <input type="number" class="form-control" id="ItemCounter" name="ItemCounter" aria-describedby="itemcounter" placeholder="Enter the count number of the item" min="0" step="1" value="0" required="required">
                     </div>
                     <div class="form-group">
                        <input type="submit" id="submitButtonforItems" name="submitButtonforItems" value="Add Product" class="btn btn-primary">
                     </div>
                     </form>
                  </div>
            </div>
            
         </div>
         <div class="panel panel-default">
            <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse2">
                  Manage Categories</a>
               </h4>
            </div>
            <div id="collapse2" data-parent="#accordion" class="panel-collapse collapse">
            	<div class="panel-body">

                  
                  	<form action="category_adder.php" method="post" enctype="multipart/form-data">
                     <div class="form-group">
                        <label for="CategoryAdder">Add Category</label>
                        <input type="text" class="form-control" id="CategoryAdder" name="CategoryAdder" aria-describedby="categoryadder" placeholder="Enter the item Category. No more than 255 symbols" required="required" size="50">
                     </div>
                     <div class="form-group">
                        <input type="submit" id="submitButtonforCategories" name="submitButtonforCategories" type="submit" value="Add Category" class="btn btn-primary">
                     </div>
                  </form>
                  <form action="category_editor.php" method="post" enctype="multipart/form-data">
                     <div class="form-group">
                     <label for="ItemCategoryOldName">Old Category Name</label>
                     <br>
                     <select name="ItemCategoryOldName" id="ItemCategoryOldName">
                     <?php
						$result = $mysqli->query("SELECT * FROM categories");
						if($result->num_rows > 0)
                     {
                  while($row = $result->fetch_array(MYSQLI_BOTH))
						{
                        echo "<option value='".$row['category']."'>".$row['category']."</option>";
						}
                     }
						?>
						</select>
					<br>
                     <br>
                        <label for="CategoryEditor">New Category Name</label>
                        <input type="text" class="form-control" id="ItemCategoryNewName" name="ItemCategoryNewName" aria-describedby="itemcategorynewname" placeholder="Enter the new item Category name. No more than 255 symbols" required="required" size="50">
                     </div>
                     <div class="form-group">
                        <input type="submit" id="submitButtonforCategoryEditor" name="submitButtonforCategoryEditor" type="submit" value="Rename Category" class="btn btn-primary">
                     </div>
                  </form>
                  <table border="1">
	<tr>
	<td><b>Category</b></td>
	</tr>
	<?php
	$result = $mysqli->query("SELECT * FROM categories");
   if($result->num_rows > 0){
   while($row = $result->fetch_array(MYSQLI_BOTH)) {
	?>
	<form action="" method="post" enctype="multipart/form-data">
	<tr>
	<td><?php echo $row["category"] ?><input type="hidden" name="<?php echo $row["category"] ?>" value="<?php echo $row["category"] ?>"><a href='delete-category-process.php?delete_category_name=<?php echo $row["category"] ?>'><i class="fas fa-ban" title="Remove Category"></i></a></td>
	</tr>
	</form>
	<?php
	}
}
	?>
</table>
<br>

<table border="1">
	<tr>
	<td class="text-center"><b>Items</b></td>
	<td class="text-center"><b>Categories</b></td>
	</tr>
	<?php
	$result = $mysqli->query("SELECT * FROM items_and_categories");
   if($result->num_rows > 0){
	while($row = $result->fetch_array(MYSQLI_BOTH)) {
	?>
	<form action="" method="post" enctype="multipart/form-data">
	<tr>
	<td class="text-center"><?php echo $row["id"] ?></td>
	<td class="text-center"><?php echo $row["category"] ?><input type="hidden" name="<?php echo $row["category"] ?>" value="<?php echo $row["category"] ?>"><a href='delete-item-and-category-process.php?delete_id=<?php echo $row["id"] ?>&delete_category_name=<?php echo $row["category"] ?>'><i class="fas fa-ban" title="Remove Item and Category Together"></i></a></td>
	</tr>
	</form>
	<?php
	}
   }
	?>
</table>

         </div>
         </div>
         </div>
         <div class="panel panel-default">
            <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse3">
                  Update/Delete Items</a>
               </h4>
            </div>
            <div id="collapse3" data-parent="#accordion" class="panel-collapse collapse">
               <div class="panel-body">
                  <form action="" method="post" enctype="multipart/form-data">
               	<table border="1">
	<tr>
	<th class="text-center">ID</th>
	<th class="text-center">Name</th>
	<th class="text-center">Description</th>
	<th class="text-center">Price</th>
	<th class="text-center">Filepath</th>
	<th class="text-center">Activation Status</th>
	<th class="text-center">Item Count</th>
	<th class="text-center">Editing Column</th>
	</tr>
   
	<?php
	$result = $mysqli->query("SELECT * FROM items");
   if($result->num_rows > 0){
   while($row = $result->fetch_array(MYSQLI_BOTH)) {
	?>
	<tr>
	<td class="text-center"><?php echo $row["id"] ?><a href='delete-id-process.php?delete_id=<?php echo $row["id"] ?>'><i class="fas fa-ban" title="Remove File"></i></a></td>
	<td class="text-center"><?php echo $row["name"] ?></td>
	<td class="text-center"><?php echo $row["description"] ?></td>
	<td class="text-center"><?php echo $row["price"] ?></td>
	<td class="text-center"><?php echo $row["filepath"] ?></td>
	<td class="text-center"><?php echo $row["activation_status"] ?></td>
	<td class="text-center"><?php echo $row["item_count"] ?></td>
	<td class="text-center"><a href='edit-id-page.php?edit_id=<?php echo $row["id"] ?>'><i class="fas fa-edit" title="Edit the Item"></i></a><a href='activation-process.php?activate_id=<?php echo $row["id"] ?>'><i class="fab fa-creative-commons-sampling" title="Change the activation status of the item"></i></a></td>
	</tr>
	
	<?php
	}
   }
	?>
</table>
</form>

               </div>
            </div>
         </div>
         <div class="panel panel-default">
            <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse4">
                  View/Manage Orders</a>
               </h4>
            </div>
            <div id="collapse4" data-parent="#accordion" class="panel-collapse collapse">
               <div class="panel-body">
               	                  <table border="1">
	<tr>
	<th class="text-center">Order ID</th>
	<th class="text-center">Order Price</th>
	<th class="text-center">Order TimeStamp</th>
	</tr>
	<?php
	$result = $mysqli->query("SELECT * FROM orders");
   if($result->num_rows > 0){
	while($row = $result->fetch_array(MYSQLI_BOTH)) {
	?>
	<form action="" method="post" enctype="multipart/form-data">
	<tr>
	<td class="text-center"><?php echo $row["order_id"] ?></td>
	<td class="text-center"><?php echo $row["order_price"] ?></td>
	<td class="text-center"><?php echo $row["order_time"] ?><a href='delete-order-process.php?delete_order_name=<?php echo $row["order_id"] ?>'><i class="fas fa-ban"></i></a></td>
	</tr>
	</form>
	<?php
	}
}
	?>
</table>

               </div>
            </div>
         </div>
      </div>
      <div><a href="logout.php">Log Out</a></div>
   </body>
</html>

