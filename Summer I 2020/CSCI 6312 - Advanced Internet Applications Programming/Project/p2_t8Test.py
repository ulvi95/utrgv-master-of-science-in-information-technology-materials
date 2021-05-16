#!/usr/bin/python
import requests #import JSONRequests library
import time #import time library for sleep function
import datetime #import datetime library for timestamp
import RPi.GPIO as GPIO #import GPIO library
GPIO.setmode(GPIO.BCM) #set the pins according to BCM scheme
GPIO.setup(4,GPIO.OUT) #configure BCM Pin #4 as OUTPUT
GPIO.setup(17,GPIO.IN) #configure BCM Pin #17 as INPUT
i=0; n=3; delay=5  #limit number of tries to 5 (initially set it to 1 for debugging)
while i<n:
	LED1=GPIO.input(4) #read what BCM Pin #4 is set to (LED1)
	SW1=GPIO.input(17) #read the status of BCM Pin #17 (SW1)
	data = {'username': 'Test', 'password': 'Tester3', 'SW1': SW1, 'LED1': LED1}
	res = requests.post("https://team2project3342.online/scripts/sync_rpi_data.php", json=data)
	#in case of errors (especially, syntax) , you may want to print res.text and comment out the statements below
	r = res.json()
	ts = datetime.datetime.now() #get the time stamp
	print "==============Server Response at " + str(ts) + "=============="
	if r['success']==1:
		print "+++++Server request successful: "
	if LED1!=r['LED1']:
		print "Changing LED status as requested by the server"
		if r['LED1']==1:
			GPIO.output(4,GPIO.HIGH)
		else: GPIO.output(4,GPIO.LOW)
		print "The status of LED1 is " + str(r['LED1'])
		print "The status of SW1 is " + str(r['SW1'])
	else: print ">>>>> Server request failed - Error #" + str(r['error'])
	time.sleep(delay) #wait for delay seconds before sending another request
	i+=1
GPIO.cleanup()