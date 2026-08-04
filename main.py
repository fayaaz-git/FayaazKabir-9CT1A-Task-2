# import stuff here

# setup here 

blueL = 1
greenL = 1
yellowL = 0
redL = 0
buzzer = 0
boundary = 147

# clear_outputs function here

def clear_outputs(a, b, c, d):
    a = 0
    b = 0
    c = 0
    d = 0

# flame_detected function here

def flame_detected(x, y):
    x = 1
    y = 1

# potential_flame function here

# all other necessary functions here

# main routine here


clear_outputs(greenL, yellowL, redL, buzzer)
sensor_values = float(input("sensor\n"))
if sensor_values >= 147:
    clear_outputs(greenL, yellowL, redL, buzzer)
    flame_detected(redL, buzzer)                    # This isn't working for some reason, the variables still remain at 0 rather than 1.
    print(redL, buzzer)
elif sensor_values >= (147 - 12):
    print("potential_flame")
else:
    print("all_ok")