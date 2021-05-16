//Below is the Java Script for the webpage with "mouseover" detection and respective action
head1 = document.getElementById("head1");
list1 = document.getElementById("list1").getElementsByTagName("li");
function f1() {
head1.innerHTML = this.innerHTML;
}

for(i=0;i<list1.length;i++) {
list1[i].addEventListener("mouseover",f1);
document.getElementById("head1").innerHTML = prompt("Suggest another heading");
}


function f2() {
let v1 = document.getElementById("user");
let v2 = document.getElementById("age");
if(v1.value == "") {
alert("Error: Field may not be left empty.");
v1.style.border = "solid 2px red";
return false;
}
else v1.style.border = "solid 1px grey";
if(v2.value == "") {
alert("Error: Field may not be left empty.");
v2.style.border = "solid 2px red";
return false;
}
else v2.style.border = "solid 1px grey";
if ((parseInt(v2.value) < 18) || (parseInt(v2.value) > 100)) {
alert("Error: Age is supposed to be between 18 and 100.");
v2.style.border = "solid 2px red";
return false;
}
else {alert("Ok ... Values are acceptable and we will process the form."); return true;}
}