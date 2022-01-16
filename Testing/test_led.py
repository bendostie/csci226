"""test LED and button setup connected to RPi
"""
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

led = 18
button = 19
GPIO.setup(button,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.output(led, True)
print(GPIO.input(button))
time.sleep(3000)
GPIO.cleanup()