import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 18
button = 19
GPIO.setup(button,GPIO.IN)
GPIO.setup(led,GPIO.OUT)

#lower bounds in milliseconds
w_adj = .25
r_adj = 1
dot_time = 100*r_adj
dash_time = 300*r_adj
word_space_time = 700*r_adj
letter_space_time = 300*r_adj
char_space_time = 100*r_adj

#latin to morse code dictionaries
morse_dict = {"_":" ", ".-":"a", "-...":"b", "-.-.":"c", "-..":"d", ".":"e", "..-.":"f", "--.":"g", "....":"h", "..":"i", ".---":"j", "-.-":"k", ".-..":"l", "--":"m", "-.":"n", "---":"o", ".--.":"p", "--.-":"q", ".-.":"r", "...":"s", "-":"t", "..-": "u", "...-":"v", ".--":"w", "-..-":"x", "-.--":"y", "--..":"z"}
latin_dict = {v: k for k, v in morse_dict.items()}


def ms_time():
    return int(round(time.time() * 1000))

def parse_letter(c, dictionary):
    
    return dictionary.get(c, "?")

def led_print(sentence, dictionary, adj):
    #l refers to latin character or series of dots and dashes that represent a latin character
    #c refers to individual dot, dash, or time spaces
    def print_letter(l):
        for c in l:
            time_dict = {'-':(1, 3), '.':(1, 1), ' ':(0, 1), '_':(0, 5)}
            c_t = time_dict.get(c)
            GPIO.output(led, c_t[0]) 
            time.sleep(c_t[1]*adj)
            GPIO.output(led, 0)
            time.sleep(1*adj)
    
    for l in sentence:
        l_m = dictionary.get(l, "_")
        print(l)
        print_letter(l_m)
        #inter-character spaces
        print_letter(" ")
        
        
    
        
        

last_state = GPIO.input(button)
state_entered = ms_time()
letter = ""

led_print("type your letter", latin_dict, w_adj)

while True:
    #wait for letter input and print. Checks time on button up event
    if (last_state != GPIO.input(button)):
        state_duration = ms_time()- state_entered
        if last_state: #button up event
            if state_duration > dash_time:
                letter += "-"
                state_entered = ms_time()
                last_state = False
            elif state_duration > dot_time:
                letter+= "."
                state_entered = ms_time()
                last_state = False
        else:              #button down event (check
            if state_duration > word_space_time: #parse letter and add space
                print(parse_letter(letter, morse_dict))
                letter = ""
                state_entered = ms_time()
                last_state = True
            elif state_duration > letter_space_time: #parse letter
                print(parse_letter(letter, morse_dict))
                letter = ""
                state_entered = ms_time()
                last_state = True
            elif state_duration > char_space_time:
                state_entered = ms_time()
                last_state = True
                
GPIO.cleanup()
