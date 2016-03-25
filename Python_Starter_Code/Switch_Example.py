import RPi.GPIO as GPIO
import time
import signal
import subprocess
import os

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

def Start_Code():
    running = 0
    while True:
        input_state = GPIO.input(12)
        if input_state == False and running == 0:
            print('On')
            blink_proc = subprocess.Popen("/home/pi/Self_Driving_Car_Project/SDRC_Project/SDRC_Project/Python_Starter_Code/Blink_Tri.sh", shell=True, preexec_fn=os.setsid)
            time.sleep(0.2)
            running = 1
        elif input_state == True and running == 1:
            print('Off')
            os.killpg(blink_proc.pid, signal.SIGTERM)
            blink_proc = None
            GPIO.output(40,False)
            GPIO.output(38,False)
            GPIO.output(36,False)
            time.sleep(0.2)
            running = 0
    return;

Start_Code()
