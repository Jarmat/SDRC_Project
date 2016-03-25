import RPi.GPIO as GPIO
import time
import Blink_LED

from Blink_LED import Blink_Tri

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

def Start_Code():
    while True:
        input_state = GPIO.input(12)
        if input_state == False:
            print('On')
            time.sleep(0.2)
        elif input_state == True:
            print('Off')
            time.sleep(0.2)
        Blink_Tri(input_state)    
    return input_state;

Start_Code()
