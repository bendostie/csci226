#Benjamin Dostie
#uses one_wire digital temp sensor and relay to make a thermostat
#set relay pin in constructor, default in the example is 19

from one_wire_temp import DS18B20 as Temp
from relay import Relay
import time

class Thermostat:
    def __init__(self, heater_pin, threshold = 2.5, one_wire = True):
        self.heat_pin = heater_pin
        self.one_wire = one_wire
        self.temp = 72.5
        self.relay = Relay(heater_pin)
        self.threshold = threshold
        if one_wire:
            self.thermometer = Temp()
    def set_temp(self, temp, celsius = False):
        if celsius:
            temp = (temp - 32) * (5/9)
        self.temp = temp
        self.poll()
    def set_threshold(self, threshold, celsius = False):
        if celsius:
            threshold = threshold * 5/9
        self.threshold = threshold
    def poll(self):
        temp = self.thermometer.read()
        
        if  temp - self.temp > self.threshold:
            
            self.relay.off()
        elif self.temp - temp > self.threshold:
            self.relay.on()

if __name__ == "__main__":
    test = Thermostat(19)
    test.set_temp(74.5)
    test.set_threshold(1)
    while True:
        test.poll()
        print(test.thermometer.read())
        time.sleep(1)