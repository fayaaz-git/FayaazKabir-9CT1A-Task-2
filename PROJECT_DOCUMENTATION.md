# MECHATRONICS PROJECT DOCUMENTATION

## Requirements Outline

### Defining the Purpose

Fires can be unpredictable, highly dangerous, and unnoticeable until it's too late. However, one of the most effective ways to warn anyone of an incoming fire are smoke & fire alarms. I will design an alarm that uses a sensor to detect flames (smoke and heat) and turn on LEDs if a fire is detected, alerting anyone in the vicinity.

### Key Actions

* Green LED remains on if nothing is detected.
* Blue LED remains on as long as the machine is on.
* Red LED starts remains on and Green LED turns off if a fire is detected.

### Functional Requirements

* **Power Detection & Alerts**: If the machine is powered on, the Blue LED also stays on (so that users are aware the alarm is powered).
* **Fire Detection & Alerts**: If the sensor values are above boundary (have yet to determine), Red LED turns on.
* **Neutral and Warning Alerts**: If the sensor values are within the boundary, Green LED turns on and stays on.

### Non-Functional Requirements

* **Response Time**: The machine should respond as fast as possible without compromising the functionality of the code. Every 100-500 milliseconds should do (is this too overkill?)

### Test Cases

| Test Case | Input | Expected Result |
|-----------|-------|-----------------|
| There is currently no fire | Flame sensor detects values within boundary | Green LED turns on |
| Machine is plugged in | Machine gains power | Blue LED turns on |
 
## Algorithms

### Pseudocode
```
BEGIN clear_outputs()  
    yellow_led.off  
    red_led.off  
    green_led.off  
    buzzer.off  
END clear_outputs()  
  
BEGIN flame_detected()  
    clear_outputs()  
    red_led.on  
    buzzer.on  
END flame_detected()  
  
BEGIN potential_flame()  
    clear_outputs()  
    yellow_led.on  
    WHILE true THEN  
        buzzer.on  
        wait(1)  
        buzzer.off  
        wait(1)  
    ENDWHILE  
END potential_flame()  
  
BEGIN  
clear_outputs()  
blue_led.on  
    WHILE true THEN  
        READ sensor_values  
        IF sensor_values >= boundary  
            flame_detected()  
        ELSE THEN  
            IF sensor_values >= (boundary - 2) THEN  
                potential_flame()  
            ELSE THEN  
            green_led.on  
            ENDIF  
        ENDIF  
    ENDWHILE  
END
```
### Flowcharts

![Subroutine Flowchart](images/9CT1A_Assessment_Task_2_Subroutine_Flowchart_Image.png)
![Main Routine Flowchart](images/9CT1A_Assessment_Task_2_Main_Routine_Functions.png)

## Testing and Debugging

### Test Case 1: Receiving Sensor Values

**14/08** - Test case failed miserably. Turns out I have no idea how to wire it up - all I know is that Ground goes into the negative output (I did some circuit stuff in Engineering), but it makes no sense because there are *four pins* - a positive one (pretty easy), a ground one, a DO pin (???) and AO (???).

```

from machine import Pin # this is where you control inputs and outputs in a Pico
import time
sensor_pin = ADC(26) """This pin is connected to the ground pin of the pico"""

"""Gonna try to test the flame sensor here.
Hopefully it works, I need to see what values they hold"""

sensor_values = sensor_pin.read_u16()				"""I'm pretty sure this receives sensor values?"""
print(sensor_values)

"""while True:
    sensor_value = sensor_pin.read_u15()	# Supposed to read the value the sensor receives
    print(sensor_value)
    time.sleep(0.5)"""
```

**18/08** - Finally figured out that AO and DO stand for analog and digital inputs. Me and my partner did some testing and THE WIRING FINALLY WORKS - we finally got some values from the sensor!

### Test Case 2: Blue LED On Upon Machine On

**18/08** - Did it first try. It was much easier than I expected. You don't even need code, since there is a pin that just outputs power constantly on the Pico.

### Test Case 3: Warining (Red LED) and Neutral (Green LED) Alerts

**19/08** - Code was easy, but the wiring was a pain in the neck. Turns out when you list a pin number in Thonny, it refers to GPIO pins rather than the physical pin itself, and GND pins don't cooperate. Finally though, I got the green and red LEDs to work... mostly, as the Red LED seems to remain constantly on despite the sensor and Green LED working completely fine.

``` 

# function setup here

"""x and y represents pins 14 and 15, respectively
as you can guess, this turns off all outputs - the green and red LEDs and the buzzer"""

def clear_outputs(x, y):	
    x.value(0)				# pin 14 turns off
    y.value(0)				# pin 15 turns off

def flame_detected(a, b):	# a and b represents the same aforementioned pins
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
       
```

**20/08** - Incorporated the buzzer. Will have to test it at home, because I don't think the teacher wil allow fires in the computer lab.

**20/08** - Turns out the buzzer doesn't work as planned, despite wiring it correctly (as in, the same way as the LEDs). Because of this I have dropped it from the functional requirements. The LEDs however, work perfectly.

```

# function setup here

"""x, y and z represents GPIO pins 14, 15, and 13 respectively
as you can guess, this turns off all outputs - the green and red LEDs and the buzzer"""

def clear_outputs(x, y):	
    x.value(0)				# pin 14 turns off
    y.value(0)				# pin 15 turns off

def flame_detected(a, b):	# a, b and c represents the same aforementioned pins
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
       

```

### Test Case 4: Potential Flame Warnings (Yellow LED)

**19/08** - When I initially wrote out my functional and non-functional requirements, I believed that actual analog values rather than two digital values would exist (thinking about it now it doesn't make sense - what else would a 'flame sensor' detect?). This is why I included the idea of a yellow LED that flashes on if the values are near the boundary (within 2 values of the boundary, as planned). However, as I started wiring up the entire machine, I discovered that the yellow LED would be completely unfeasible, and therefore I have dropped it from the functional requirements.

## Evaluations

### Peer Eval

| Evaluator | Plus | Minus | Implication |
|-----------|------|-------|-------------|
| Ronav M   | Flame sensor system is able to detect presence of flames in vicinity, alerting the user using led lights, with green reflecting that status is safe while the red led alerts the user that a fire has been detected in surroundings, working without malfunctioning and detecting the smallest traces of fire. | The red LED occasionally flickers randomly, which is a bit misleading | The flame sensor system using wiring and coding was succesfully able to detect and alert the user about presence of fire in surroundings, shwoing how functional and sophiticated this project is |
| Alfonso D | The use of diffrent coloured LEDs is smart, allowing the user to clearly understand the machine | Code could be more clean and the commments could be more descriptive   | Blue LED turns on |

### Final Eval

#### In Relation to Functional Criteria

The machine meets all functional criteria stated in the Requirements Outline. The Blue LED remains on if the machine is on, and the Green and Red LEDs turn on depending on whether a fire is not or is detected, respectively. However, some criteria have been removed from the Requirements Outline as they cannot be feasibly achieved due to the design of the sensor. 

#### In Relation to Non-Functional Criteria

The machine meets all non-functioning criteria, as the response time of the machine is 500 milliseconds. Similar to the functional criteria, some non-functioning criteria has been removed from the non-functioning criteria as they are unfeasible and also don't have an impact on overall functionability. The response time also doesn't have a negative impact on the machine and I don't believe it is 'overkill'.

#### In Relation to the Purpose

The machine achieves the purpose as planned. It works well as a fire alarm as it detects fires using a sensor and alerts people in the vicinity using lights. Auditory alerts would have improved the project more and would have been incorporated into the machine if it weren't for time constraints.

#### In Relation to Project Management

The machine works rather well compared to its project management. It works as planned despite time constraints. However, such time constraints have also impacted some other functional and non-functional requirements, most notably the inclusion of buzzers into the design.

#### In Relation to Peer Feedback

The peer feedback identifies many positives and issues that the machine has. The overall functionability with the blue, red and green LEDs have been noted as a good inclusion, with minor issues mainly involving the code and notes on the code. 

#### Future Improvements on Final Product

If I could include more features to my machine, an auditory alert via a buzzer would definitely be at the top of my list. As a fire alarm warning, it would be beneficial, as auditory alerts are more effective compared to visual alerts. However, as noted previously time constraints have affected the proper inclusion of such an alert.