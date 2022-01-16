"""attempts to keep dot in same place using accelerometer and gyro of RPi sense hat"""
from sense_hat import SenseHat
import time
import math
from statistics import mean
sense = SenseHat()
x = 0
y = 4
adj = 10

velocity_x = 0
velocity_y = 0

while True:
    acceleration = sense.get_accelerometer_raw()
    new_x = acceleration['x']
    new_y = acceleration['y']
    new_z = acceleration['z']
    o = sense.get_orientation()
    pitch = o["pitch"]
    roll = o["roll"]
    yaw = o["yaw"]
    
    #get velocity ignoring gravitational acceleration 
    gravity_x = -.988 * math.sin(math.radians(pitch))
    gravity_y = .9851 * math.sin(math.radians(roll))
    
    accl_x = new_x - gravity_x
    accl_y = new_y - gravity_y
    
    #print(accl_x)
    
    velocity_x += accl_x
    velocity_y += accl_y
    
    
    
    
    #deal with saturation and out of bound values
    if x==0 and velocity_x < 0:
        velocity_x = 0
    elif x==7 and velocity_x > 0:
        velocity_x = 0
        
    print(velocity_x)
    x = max(min( x + velocity_x, 7), 0)
    
    if y==0 and velocity_y < 0:
        velocity_x = 0
    elif y==7 and velocity_y > 0:
        velocity_x = 0
    
    y = max(min( y + velocity_y, 7), 0)
        
    
    sense.clear()
    sense.set_pixel(int(x), int(y), (0, 0, 255))
    #old_x = new_x
    #old_y = new_y
    
    #print("x' {0} pitch {1}  x {2} z{3}".format(new_x - (-.995 * math.sin(math.radians(pitch))), pitch, new_x, new_z))
    #print("pitch {0} roll {1}  x {2}".format(pitch, roll, new_x))
    #print(new_y - (-.9851 * math.sin(math.radians(roll))))
    

