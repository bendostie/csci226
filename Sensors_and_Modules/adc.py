# based on code written by Limor "Ladyada" Fried for Adafruit Industries, (c) 2015
# https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Raspberry_Pi_DS18B20_Temperature_Sensing/code.py

import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

class ADC:
    def __init__(self, CLK= 18, MISO = 23, MOSI = 24, CS = 25):
         
        # change these as desired - they're the pins connected from the
        # SPI port on the ADC to the Cobbler

        self.clockpin  = CLK
        self.misopin = MISO
        self.mosipin = MOSI
        self.cspin   = CS
         
        # set up the SPI interface pins
        GPIO.setup(self.mosipin, GPIO.OUT)
        GPIO.setup(self.misopin, GPIO.IN)
        GPIO.setup(self.clockpin, GPIO.OUT)
        GPIO.setup(self.cspin, GPIO.OUT)

        VREF = 3.3
    def read(self, sensor_number):
        #make sure sensor  is in range
        if ((sensor_number > 7) or (sensor_number < 0)):
            return -1
        
        GPIO.output(self.cspin, True)      # set CS high (if not already high)
        GPIO.output(self.clockpin, False)  # start clock low
        GPIO.output(self.cspin, False)     # bring CS low
 
        commandout = sensor_number
        commandout |= 0x18  # start bit + single-ended bit
        commandout <<= 3    # we only need to send 5 bits here
        for i in range(5):
            if (commandout & 0x80):
                GPIO.output(self.mosipin, True)
            else:
                GPIO.output(self.mosipin, False)
            commandout <<= 1
            GPIO.output(self.clockpin, True)                
            GPIO.output(self.clockpin, False) 
        adcout = 0
        # read in one empty bit, one null bit and 10 ADC bits
        for i in range(12):                
            GPIO.output(self.clockpin, True)                
            GPIO.output(self.clockpin, False)                
            adcout <<= 1
            if (GPIO.input(self.misopin)):
                        adcout |= 0x1
 

        GPIO.output(self.cspin, True)

        adcout >>= 1       # drop the last bit, i.e. the stop bit
                           # the start bit is 0 so we can ignore it
        return adcout

if __name__ == "__main__":
    test = ADC()
    
    while True:
        
        print(test.read(0))
        time.sleep(1)
