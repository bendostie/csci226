#Benjamin Dostie
#uses MCP3008 and Relay to turn on pump when water is detected
#check adc.py for default SPI pin numbers


from adc import ADC as Sense
from relay import Relay
import time

class SubPump:
    def __init__(self, pump_pin, threshold = 100):
        self.pump = Relay(pump_pin)
        self.sensor = Sense()
        self.threshold = threshold
        self.last_checked = time.time()
        self.last_value = self.sensor.read(0)
    
    def poll(self):
        water = self.sensor.read(0)
        print("difference: ", water - self.last_value)
        if  1/abs(self.last_checked - time.time()) * water - self.last_value > self.threshold:
            self.pump.on()
        elif water < self.threshold:
            self.pump.off()
        self.last_value = water
        self.last_checked = time.time()

if __name__ == "__main__":
    test = SubPump(19)
    
    while True:
        test.poll()
        print(test.sensor.read(0))
        time.sleep(1)