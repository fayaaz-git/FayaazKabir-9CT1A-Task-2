# import stuff here

from machine import Pin
import time

# setup here 

# clear_outputs function here

def clear_outputs(g, y, r, b):
    g = 0
    y = 0
    r = 0
    b = 0

# flame_detected function here

def flame_detected(r, b):
    while r == 0:
        r = r + 1
    while b == 0:
        b = b + 1
        print(b)

# potential_flame function here

def potential_flame(y, b):
    clear_outputs(greenL, yellowL, redL, buzzer)
    while y == 0:
        y = 1
    while y == 1:


# all other necessary functions here

# main routine here

led = Pin(15, Pin.OUT)	# Sets up pin 15 to power in order to turn on the blue LED
led.value(1)			# Turn on the pin
