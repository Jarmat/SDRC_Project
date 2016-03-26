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

def my_callback(channel):
    input_state = GPIO.input(12)

    return input_state;

def Blink_Red():
    GPIO.output(40,True)
    time.sleep(0.5)
    GPIO.output(40,False)
    time.sleep(0.5)

    return:

def Start_Code():
    running = 0
    while True:
        input_state = GPIO.input(12)
        if input_state == False and running == 0:
            GPIO.output(40,False)
            print('On')
            blink_proc = subprocess.Popen("/home/pi/Self_Driving_Car_Project/SDRC_Project/SDRC_Project/Python_Starter_Code/Blink_Tri.sh", shell=True, preexec_fn=os.setsid)
            time.sleep(0.2)
            running = 1

        while input_state == True:
            if running == 1:
                GPIO.output(40,False)
                GPIO.output(38,False)
                GPIO.output(36,False)
                print('Off')
                os.killpg(blink_proc.pid, signal.SIGTERM)
                blink_proc = None

                GPIO.cleanup()
                GPIO.setmode(GPIO.BOARD)

                GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
                GPIO.setup(40, GPIO.OUT)
                GPIO.setup(38, GPIO.OUT)
                GPIO.setup(36, GPIO.OUT)

                GPIO.output(38,False)
                GPIO.output(36,False)
                running = 0

            input_state = GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback)
            Blink_Red()

    return;



try:
    Start_Code()
except KeyboardInterrupt:
    GPIO.cleanup()
