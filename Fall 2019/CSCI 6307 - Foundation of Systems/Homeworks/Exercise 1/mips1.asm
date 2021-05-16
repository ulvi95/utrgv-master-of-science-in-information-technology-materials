.data
startText: .asciiz "               THIS IS CONVERT FROM FAHRENHEIT TO CELCIUS               \n\n"

promptText: .asciiz "Enter degrees in Fahrenheit: \n"
fahrenText: .asciiz "Stored in RAM Fahrenheit: "
finalText: .asciiz "\nThe temperature in Celsius is "

Minus: .float 32
Multip: .float 5
Divide: .float 9

Fahrenheit: .float 0
Celsius: .float 0

.text
li $v0, 4
la $a0, startText
syscall

li $v0, 4
la $a0, promptText
syscall

#input Fahrenheit from keyboard
li $v0, 6
syscall

swc1 $f0, Fahrenheit
l.s $f1, Minus
l.s $f2, Multip
l.s $f3, Divide

#formula for convertion
sub.s $f0, $f0, $f1
mul.s $f0, $f0, $f2
div.s  $f0, $f0, $f3
s.s $f0, Celsius

#display input and results (P.S float output register assigned to $f12 in the options of MARS 4.5 in advance. In other case, program shows 0.0 for both values)
li $v0, 4
la $a0, fahrenText
syscall

li $v0, 2
l.s $f12, Fahrenheit
syscall

li $v0, 4
la $a0, finalText
syscall

li $v0, 2
l.s $f12, Celsius
syscall

li $v0, 10
syscall
