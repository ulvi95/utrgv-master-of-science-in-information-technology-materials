<?php
$t = 5;

if ($t < 6) {
  echo "$t is smaller than 6<br>";
}
?>
<?php
$t = 7;

if ($t < 6) {echo "$t is smaller than 6<br>";}
else 
{echo "$t is not smaller than 6<br>";}
?>
<?php
$t = 6;

if ($t < 6) {echo "$t is smaller than 6<br>";}
elseif ($t === 6) {echo "t is equal to 6<br>";}
else {echo "$t is not smaller than 6<br>";}
?>

<?php
$favcolor = "blue";

switch ($favcolor) {
  case "red":
    echo "Your favorite color is red!<br>";
    break;
  case "blue":
    echo "Your favorite color is blue!<br>";
    break;
  case "green":
    echo "Your favorite color is green!<br>";
    break;
  default:
    echo "Your favorite color is neither red, blue, nor green!<br>";
}
?>