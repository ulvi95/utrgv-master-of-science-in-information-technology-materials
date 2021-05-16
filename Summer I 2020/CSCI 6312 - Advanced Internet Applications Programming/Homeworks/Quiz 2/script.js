
function calculation()
{
var FirstOperand = document.getElementById("FirstOperand");
var SecondOperand = document.getElementById("SecondOperand");
var Operator = document.getElementById("Operator");
var Result;
if(FirstOperand.value == "" || SecondOperand.value == "" || Operator.value  == "") {
alert("Error: Field may not be left empty.");
return false;
}
if ((parseInt(FirstOperand.value) < 0) || (parseInt(FirstOperand.value) >= 100 ) || (parseInt(SecondOperand.value) < 0) || (parseInt(SecondOperand.value) >= 100 ))
{
alert("Error: Numbers are supposed to be between 0 and 99 inclusive.");
return false;
}
if ((Operator.value != "+") && (Operator.value != "-") && (Operator.value != "*") && (Operator.value != "add") && (Operator.value != "sub") && (Operator.value != "mul") )
{
alert("Error: Only Addition, Substraction, and Multiplication are allowed");
return false;
}
if ( (Operator.value == "+") || (Operator.value == "add") )
{
Result = (parseInt(FirstOperand.value)) + (parseInt(SecondOperand.value))
return alert(Result);
}
if ( (Operator.value == "-") || (Operator.value == "sub") )
{
Result = (parseInt(FirstOperand.value)) - (parseInt(SecondOperand.value))
return alert(Result);
}
if ( (Operator.value == "*") || (Operator.value == "mul") )
{
Result = (parseInt(FirstOperand.value)) * (parseInt(SecondOperand.value))
return alert(Result);
}
}