# GPIO controls

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	

GPIO.setup(4, GPIO.IN)
GPIO.setup(17, GPIO.IN)
GPIO.setup(27, GPIO.IN)
GPIO.setup(22, GPIO.IN)

def button_a():
	return GPIO.input(4) == True
def button_b():
	return GPIO.input(17) == True
def button_y():
	return GPIO.input(27) == True
def button_x():
	return GPIO.input(22) == True