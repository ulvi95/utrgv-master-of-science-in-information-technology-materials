<html>
<body>
<form action="" method="post">
Name: <input type="text" name="name"><br>E-mail: <input type="text" name="email"><br><input type="submit" name="SubmitButton">
</form>
<?php 
if(isset($_POST['SubmitButton']))
{echo "Welcome: " . $_POST["name"] . "<br>" . "Your email address is: " . $_POST["email"] ;}
?>
</body>
</html> 