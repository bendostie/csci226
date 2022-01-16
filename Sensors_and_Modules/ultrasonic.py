import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger = 23
echo = 24

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.output(trigger, False)
print("waiting for sensor to settle")
time.sleep(2)
def distance():
    
        #pulse trigger
    GPIO.output(trigger, True)
    time.sleep(0.00001)
    GPIO.output(trigger, False)
        
    start_time = time.time()
    stop_time = time.time()
        
    while not GPIO.input(echo):
        start_time = time.time()
    while GPIO.input(echo):
        stop_time = time.time()
    time_elapsed = stop_time - start_time
    distance = (time_elapsed * 34300)/2
    return distance
if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured distance = %.1f cm" %dist)
            time.sleep(1)
    except KeyboardInterrupt:
        print("stpped by user")
        GPIO.cleanup()
            