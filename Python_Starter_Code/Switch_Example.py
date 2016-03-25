import RPi.GPIO as GPIO
import time
import subprocess

from subprocess import Popen

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
    input_state = GPIO.input(12)
    if input_state == False:
            print('On')
            time.sleep(0.2)
            process = Popen(["Blink", "Blink_LED.py"])
        elif input_state == True:
            print('Off')
            time.sleep(0.2)
            process = Popen.kill(["Blink", "Blink_LED.py"])
