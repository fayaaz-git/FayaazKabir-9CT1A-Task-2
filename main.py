def clear_outputs(x, y):
    x.value(0)
    y.value(0)

def flame_detected(a, b):
    print('flame')				
    a.value(0)
    b.value(1)

# import everything needed
from machine import Pin
import time

sensor_pin = Pin(16, Pin.IN, Pin.PULL_DOWN)		# this is the pin that reads sensor values

green_led = Pin(14, Pin.OUT)
red_led = Pin(15, Pin.OUT)

"""For lines 16 and 20 (I can't write it within the while loop because it throws off Thonny's indentation thingy):
the print value checks if the sensor properly works (by printing it in the shell where only I can check)"""

while True:
    time.sleep(0.5)					# small break between flame detections
    if sensor_pin.value() == 1:
        clear_outputs(green_led, red_led)
        flame_detected(green_led, red_led)
    else:
        print("no flame")
        clear_outputs(green_led, red_led)
        green_led.value(1)
       
