"""attempts to keep dot in same place using accelerometer and gyro of RPi sense hat"""
from sense_hat import SenseHat
import time
import math
from statistics import mean
sense = SenseHat()
x = 0
y = 4
adj = 10
acceleration = sense.get_accelerometer_raw()
#old_x = acceleration['x']
#old_y = acceleration['y']
#old_z = acceleration['z']

new_ylist = []
while True:
	acceleration = sense.get_accelerometer_raw()
	new_x = acceleration['x']
	new_y = acceleration['y']
	new_z = acceleration['z']
	o = sense.get_orientation()
	pitch = o["pitch"]
	roll = o["roll"]
	yaw = o["yaw"]
	
	x = min(max((new_x )*adj + x, 0.0), 7.0)
	y = min(max((new_y)*adj + y, 0.0), 7.0)
	sense.clear()
	sense.set_pixel(int(x), int(y), (0, 0, 255))
	#old_x = new_x
	#old_y = new_y
	new_ylist.append(new_x - (.988 * math.sin(math.radians(roll))))
	#print("x' {0} pitch {1}  x {2} z{3}".format(new_x - (-.995 * math.sin(math.radians(pitch))), pitch, new_x, new_z))
	#print("pitch {0} roll {1}  x {2}".format(pitch, roll, new_x))
	#print(new_x - (-.995 * math.sin(math.radians(pitch))))
	print("average", mean(new_ylist))