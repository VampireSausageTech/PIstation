import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN)
while True:
	if GPIO.input(3):
		print("hi")
		pass
