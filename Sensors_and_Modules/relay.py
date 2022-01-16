#Benjamin Dostie
#class for relay control on RPi
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class Relay:
    def __init__(self, pin):
        self.pin = pin
        self.status = False
        GPIO.setup(pin, GPIO.OUT)
    def on(self):
        GPIO.output(self.pin, GPIO.HIGH)
        self.status = True
    def off(self):
        GPIO.output(self.pin, GPIO.LOW)
        self.status = False
    
    
if __name__ == "__main__":
    test = Relay(19)
    while True:
        test.on()
        time.sleep(2)
        test.off()
        time.sleep(2)