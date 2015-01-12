# GPIO controls

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)	

GPIO.setup(23, GPIO.IN) # GPIO 4

def button_a():
	print('hawt! :3');
	print(GPIO.input(23));
	return GPIO.input(23) == True
def button_b():
	return GPIO.input(17) == True
def button_y():
	return GPIO.input(27) == True
def button_x():
	return GPIO.input(22) == True


#nieuwe code by Zohaad
#INSTRUCTIES: gebruik pip of easy_install voor python-uinput (tjjr.fi)
# aan /etc/modules toevoegen OF "modprobe uinput"

import uinput

device = uinput.Device([
	uinput.KEY_A,
	uinput.KEY_B,
	uinput.KEY_C,
	uinput.KEY_D,
	])
while True:
	if button_a():
		device.emit_click(uinput.KEY_A)
	if button_b():
		device.emit_click(uinput.KEY_B)
	if button_c():
		device.emit_click(uinput.KEY_C)
	if button_d():
		device.emit_click(uinput.KEY_D)

