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

$id = $mysqli->real_escape_string($_GET["edit_id"]);

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
                  <table>
   <tr>
   <th align="center">ID</th>
   <th align="center">Name</th>
   <th align="center">Description</th>
   <th align="center">Price</th>
   <th align="center">Filepath</th>
   <th align="center">Activation Status</th>
   <th align="center">Item Count</th>
   </tr>
   <?php
   $result = $mysqli->query("SELECT * FROM items WHERE id=$id");
   if ($result->num_rows > 0)
   {
   while($row = $result->fetch_array(MYSQLI_BOTH)) {
   ?>
   <tr>
   <td align="center"><?php echo $row["id"] ?></td>
   <td align="center"><?php echo $row["name"] ?></td>
   <td align="center"><?php echo $row["description"] ?></td>
   <td align="center"><?php echo $row["price"] ?></td>
   <td align="center"><?php echo $row["filepath"] ?></td>
   <td align="center"><?php echo $row["activation_status"] ?></td>
   <td align="center"><?php echo $row["item_count"] ?></td>
   </tr>
   <?php
   }
   }
   ?>
</table>
      <div class="panel-group btn btn-light btn-group-vertical justify-content-center" id="accordion">
         <div class="panel panel-default">
                        <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse1">
                  Change Item</a>
               </h4>
            </div>
            <div id="collapse1" data-parent="#accordion" class="panel-collapse collapse in">
                  <div class="panel-body">
<form action="edit-id-process.php" method="post" enctype="multipart/form-data">
                     <div class="form-group">
                        <input type="hidden" class="form-control" id="<?php echo $id ?>" name="ItemID" value="<?php echo $id ?>" aria-describedby="itemid">
                        <label for="ItemName">New item Name</label>
                        <input type="text" class="form-control" id="ItemName" name="ItemName" aria-describedby="itemname" placeholder="Enter the item name. No more than 255 symbols" required="required">
                     </div>
                     <div class="form-group">
                        <label for="ItemDescription">New item Description</label>
                        <textarea class="form-control" id="ItemDescription" name="ItemDescription" aria-describedby="itemdescription" placeholder="Enter the item description. No more than 1023 symbols" rows="4" cols="50" maxlength="1024"></textarea>
                     </div>
                     <div class="form-group">
                        <label for="ItemPrice">New item Price</label>
                        <input type="number" class="form-control" id="ItemPrice" name="ItemPrice" aria-describedby="itemprice" placeholder="Enter the price" min="0" max="1000" step=".01" value="0">
                     </div>
                     <div class="form-group">
                        <label for="ItemCategory">Change Category</label>
                        <select name="ItemCategory" id="ItemCategory">
                        	<?php
						$result = $mysqli->query("SELECT * FROM categories");
                     if ($result->num_rows > 0)
               {
						while($row = $result->fetch_array(MYSQLI_BOTH))
						{
                        echo "<option value='".$row['category']."'>".$row['category']."</option>";
						}
               }
						?>
						</select>
                     </div>
                     <div class="form-group">
                        <label for="ItemPicturePath">New item Picture Path</label>
                        <input type="file" class="form-control" id="ItemPicturePath" name="ItemPicturePath" aria-describedby="ItemPicturePath" placeholder="Add the product picture">
                     </div>
                     <div class="form-group">
                        <label for="ItemActivationStatus">Activation Status</label>
                        <select name="ItemActivationStatus" id="ItemActivationStatus">
                        <option value="yes">Yes</option>
                        <option value="no">No</option>
                        </select>
                     </div>
                     <div class="form-group">
                        <label for="ItemCounter">Item Count</label>
                        <input type="number" class="form-control" id="ItemCounter" name="ItemCounter" aria-describedby="itemcounter" placeholder="Enter the count number of the item" min="0" step="1" value="0">
                     </div>
                     <div class="form-group">
                        <input type="submit" id="submitButtonforItems" name="submitButtonforItems" value="Edit Product" class="btn btn-primary">
                     </div>
                     </form>
                  </div>
                     </div>
                     </div>
                             <div class="panel panel-default">
            <div class="panel-heading">
               <h4 class="panel-title">
                  <a class="card-link" data-toggle="collapse" href="#collapse2">
                  Add New Category or Delete the Category</a>
               </h4>
            </div>
            <div id="collapse2" data-parent="#accordion" class="panel-collapse collapse">
               <div class="panel-body">

                  
                     <form action="add-item-and-category-process.php" method="post" enctype="multipart/form-data">
                     <div class="form-group">
                        <input type="hidden" class="form-control" id="<?php echo $id ?>" name="ItemID" value="<?php echo $id ?>" aria-describedby="itemid">
                        <label for="CategoryAdder">Add Category</label>
                                                <select name="ItemCategory" id="ItemCategory">
                           <?php
                  $result = $mysqli->query("SELECT * FROM categories");
                  while($row = $result->fetch_array(MYSQLI_BOTH))
                  {
                        echo "<option value='".$row['category']."'>".$row['category']."</option>";
                  }
                  ?>
                  </select>
                     </div>
                     <div class="form-group">
                        <input type="submit" id="submitButtonforCategories" name="submitButtonforCategories" type="submit" value="Add Category" class="btn btn-primary">
                     </div>
                  </form>
                  
<br>

<table>
   <tr>
   <td><b>Items</b></td>
   <td><b>Categories</b></td>
   </tr>
   <?php
   $result = $mysqli->query("SELECT * FROM items_and_categories WHERE id=$id");
   if ($result->num_rows > 0)
               {
   while($row = $result->fetch_array(MYSQLI_BOTH)) {
   ?>
   <form action="" method="post" enctype="multipart/form-data">
   <tr>
   <td><?php echo $row["id"] ?></td>
   <td><?php echo $row["category"] ?><input type="hidden" name="<?php echo $row["category"] ?>" value="<?php echo $row["category"] ?>"><a href='delete-item-and-category-process.php?delete_id=<?php echo $row["id"] ?>&delete_category_name=<?php echo $row["category"] ?>'><i class="fas fa-ban" title="Remove Item and Category Together"></i></a></td>
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
                        </body>
</html>