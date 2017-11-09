import RPi.GPIO as GPIO
import pyrebase
from time import sleep

#Firebase configuration. Replace with your project specific information

config = {
	"apiKey": "YourAPIKey",
	"authDomain": "YourDomain.firebaseapp.com",
	"databaseURL": "https://YourURL.firebaseio.com",
	"storageBucket": "YourApp.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#Point to location of the Firebase database where the "switch" value will be.
#In this case, we will parse either a 0 or 1 to control the state of a relay switch.

switchStatus = db.child("Project_Home/switchOnOff").get()
print("started PyrebaseControl.py" + "\n" + "current switch status is " + switchStatus.val())

switcherPin = 10 #Replace with GPIO pins of your choice 
GPIO.setmode(GPIO.BCM)
GPIO.setup(switcherPin, GPIO.OUT)
#GPIO.output(switcherPin, GPIO.HIGH)

#This loop checks the value of the switch every 5 seconds and acts accordingly.

try:
	while True:
		swtichStatus = db.child("Project_Home/switchOnOff").get()
		sleep(1)
		status = switchStatus.val()
		if status == "1":
			GPIO.output(printerpin, GPIO.LOW)
			sleep(5)
		else:
			GPIO.output(printerpin, GPIO.HIGH)
			sleep(5)

except KeyboardInterrupt:
	print "\n"

finally:
	GPIO.cleanup()
