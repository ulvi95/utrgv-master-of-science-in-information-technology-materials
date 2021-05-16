<?php
function writeMsg() {
  echo "Hello world!<br>";
}
writeMsg(); // call the function
function Test($name, $surname) {
  echo "Hello $name $surname!<br>";
}
Test("Ulvi", "Bajarani");
function TestDefaultValue($name="John", $surname="Doe") {
  echo "Hello $name $surname!<br>";
}
TestDefaultValue("Ulvi", "Bajarani");
TestDefaultValue();
function TestAddition($a, $b) {
return $a + $b;
}
TestAddition(5, 10);
?>