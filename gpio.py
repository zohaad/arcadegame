# GPIO controls

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	

GPIO.setup(23, GPIO.IN) # GPIO 4

def button_a():
	print('heyt!');
	print(GPIO.input(23));
	return GPIO.input(23) == True
def button_b():
	return GPIO.input(17) == True
def button_y():
	return GPIO.input(27) == True
def button_x():
	return GPIO.input(22) == True
