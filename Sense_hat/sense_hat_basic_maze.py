from sense_hat import SenseHat
import time
import math
from statistics import mean
sense = SenseHat()
sense.clear()

o = (255, 0, 0) # Green
x = (0, 0, 0) # Black
w = (218,165,32)

maze1_pixels = [
    o, o, x, o, x, x, x, o,
    x, x, x, x, x, o, x, x,
    x, o, o, o, o, o, x, o,
    x, x, x, x, o, x, x, o,
    o, x, o, x, x, x, o, o,
    o, x, o, x, o, x, x, x,
    o, x, x, o, o, o, o, x,
    o, o, w, o, x, x, x, x
]

o = 0
x = 1
w = 2

maze1_paths = [
    [o, o, x, o, x, x, x, o],
    [x, x, x, x, x, o, x, x],
    [x, o, o, o, o, o, x, o],
    [x, x, x, x, o, x, x, o],
    [o, x, o, x, x, x, o, o],
    [o, x, o, x, o, x, x, x],
    [o, x, x, o, o, o, o, x],
    [o, o, w, o, x, x, x, x]
]


y = 0#y, x
x = 2

sense.set_pixels(maze1_pixels)
sense.set_pixel(x, y, (0, 255, 0))

def move(event):
    global x
    global y
    global maze1_paths
    global maze1_pixels
    if event.action == 'pressed':
        
        if event.direction == 'down':
            if y < 7 and maze1_paths[y+1][ x]:
                y += 1
        elif event.direction == 'up':
            if y > 0 and maze1_paths[y-1][ x]:
                y -= 1
            
        elif event.direction == 'right':
            if x < 7 and maze1_paths[y][ x+1]:
                x += 1
        elif event.direction == 'left':
            if x > 0 and maze1_paths[y][ x-1]:
                x -= 1
        sense.set_pixels(maze1_pixels)
        sense.set_pixel(x, y, (0, 255, 0))
        
        if maze1_paths[y][x] == 2:
            sense.show_message("YOU WIN!")
            y = 0
            x = 2
            sense.set_pixels(maze1_pixels)
            sense.set_pixel(x, y, (0, 255, 0))
sense.stick.direction_any = move
while True:
    pass

