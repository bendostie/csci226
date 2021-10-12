# from: http://www.uugear.com/portfolio/dht11-humidity-temperature-sensor-module/
# RGW Changes:
#   - Fixed the number of samples (clearly Python is running much faster)
#   - Simplified the code - reading the data and crc now use the same code
#   - Printed more debugging information, but during normal run and also in case
#     of an error.
#
# The sensor & commumication is error-prone, if you get a "Not enough data" or
# "CRC Error", just try running the program again.
#
# I would suggest running your program directly in the console, not using an IDE
#   python3 dht11_sampling.py


import RPi.GPIO as GPIO
import time

# Notice that you need a pull-up resistor if not using a pin that has
#   on internally
DATA_PIN = 4

SAMPLES = 5000
THRESHOLD = 20

def bin2dec( string_num ):
    return int( string_num, 2 )

data = []

GPIO.setmode( GPIO.BCM )

# Create a pulse on the data pin
GPIO.setup( DATA_PIN, GPIO.OUT )
GPIO.output( DATA_PIN,GPIO.HIGH )
time.sleep( 0.025 )
GPIO.output( DATA_PIN, GPIO.LOW )
time.sleep( 0.02 )

# Change to input to get the response

GPIO.setup( DATA_PIN, GPIO.IN)

for i in range( 0, SAMPLES ):
    data.append( GPIO.input( DATA_PIN ) )

high_count = 0
count = 0
bits = ""
crc = ""

try:
    # Wait one full cycle for the data
    while data[count] == 0:
        count = count + 1
        
    while data[count] == 1:
        count = count + 1

    # Read 40 bits of data - 4 data bytes and 1 crc byte
    for i in range(0, 40):
        low_count = 0
        high_count = 0

        while data[count] == 0 or low_count < 10:
            low_count = low_count + 1
            count = count + 1

        while data[count] == 1 or high_count < 10:
            high_count = high_count + 1
            count = count + 1

        if THRESHOLD < high_count:
            bits = bits + "1"
        else:
            bits = bits + "0"

        print( i, count, high_count ) # debug - print bit counts

except:
    print( "Not enough data" )
    print( i, count)
    exit(0)

humidity_high = bin2dec(bits[0:8])
humidity_low = bin2dec(bits[8:16])      # ignore for DHT11 
temperature_high = bin2dec(bits[16:24])
temperature_low = bin2dec(bits[24:32])  # ignore for DHT11
crc = bin2dec(bits[32:40])

check = ( humidity_high + humidity_low + temperature_high + temperature_low ) % 256
# check = ( humidity_high + temperature_high ) % 256

if check == crc:
    print()
    print( "Humidity:"+ str(humidity_high) +"%" )
    print( "Temperature:"+ str(temperature_high) +"C" )
else:
    print( "CRC Error" )
    print( humidity_high, humidity_low, temperature_high, temperature_low, crc )
