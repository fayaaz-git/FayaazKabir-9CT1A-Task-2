# everything required is imported here

from machine import Pin # this is where you control inputs and outputs in a 
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

led = Pin(15, Pin.OUT);	# Sets up pin 15 to power in order to turn on the blue LED
led.value(1)

"""Gonna try to test the flame sensor here.
Hopefully it works, I need to see what values they hold"""

"""sensor_pin = ADC(Pin(26));				""""""I think this pin is the one receiving the sensor values?
                                        It is the one connected to GND (Ground, I assume).
                                        The sensor is glowing green and red so hopefully it works
                                        Anyway I took this from the PWM tutorial, which uses a potentiometer.""""""

while True:
    sensor_value = sensor_pin.read_u15()	# Supposed to read the value the sensor receives
    print(sensor_value)
    time.sleep(0.5)
