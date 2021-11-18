#based on https://github.com/adafruit/Adafruit_Learning_System_Guides/blob/main/Raspberry_Pi_DS18B20_Temperature_Sensing/code.py
#enable OneWire interface in config. Use: sudo raspi-config
#connect signal to pin 4 with a 4.7k pull-up resistor
#connect 3.3v and ground
import glob
import time
class DS18B20:
    def __init__(self):
        #build filepath for sensor. Readings are stored in a file
        base_dir = '/sys/bus/w1/devices/'
        device_folder = glob.glob(base_dir + '28*')[0]
        self.device_file = device_folder + '/w1_slave'

    def read_temp_raw(self):
        #open file and read contents raw
        f = open(self.device_file, 'r')
        lines = f.readlines()
        f.close()
        return lines

    def read(self):
        #read file
        lines = self.read_temp_raw()
        #wait for YES
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = read_temp_raw()
        #once YES get temp
        equals_pos = lines[1].find('t=')
        #calculate temp in C and F
        if equals_pos != -1:
            temp_string = lines[1][equals_pos+2:]
            temp_c = float(temp_string) / 1000.0
            temp_f = temp_c * 9.0 / 5.0 + 32.0
            return temp_f
if __name__ == "__main__":
    test = DS18B20()
    while True:
        print(test.read())
        time.sleep(1)
    