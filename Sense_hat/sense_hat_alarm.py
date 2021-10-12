from sense_hat import SenseHat
import time
import math
from statistics import mean
sense = SenseHat()
sense.clear()


th = .1

# Define some colours
r = (255, 0, 0) # Green
b = (0, 0, 0) # Black

# Set up where each colour will display
alarm_pixels = [
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b
]
alarm_pixels_compliment = [
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r,
    r, b, r, b, r, b, r, b,
    b, r, b, r, b, r, b, r
]

acceleration = sense.get_accelerometer_raw()
old_x = acceleration['x']
old_y = acceleration['y']
old_z = acceleration['z']

while True:
    acceleration = sense.get_accelerometer_raw()
    
    dx = abs(old_x - acceleration['x'])
    dy = abs(old_y - acceleration['y'])
    dz = abs(old_z - acceleration['z'])
    
    if dx > th or dy > th or dz > th:
        for i in range(20):
            sense.set_pixels(alarm_pixels)
            time.sleep(.1)
            sense.set_pixels(alarm_pixels_compliment)
            time.sleep(.1)
            sense.clear()
        
    
    old_x = acceleration['x']
    old_y = acceleration['y']
    old_z = acceleration['z']