import RPi.GPIO as GPIO
import time
# import signal
# import subprocess
# import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

running = 0

GPIO.output(40,False)
GPIO.output(38,False)
GPIO.output(36,False)

def Blink_Tri():
    x = 1
    for x in range (1,10):
        GPIO.output(36,True)
        time.sleep(0.2)
        GPIO.output(36,False)
        time.sleep(0.2)
        x += 1
    GPIO.output(38,False)

    GPIO.output(38,True)

    return;


def Blink_Red():
    input_state = GPIO.input(12)
    GPIO.output(40,True)
    time.sleep(0.5)
    input_state = GPIO.input(12)
    GPIO.output(40,False)
    time.sleep(0.5)

    return;


def my_callback(channel):
    if GPIO.input(12):
        Blink_Tri()
    else:
        Blink_Red()

    return;

GPIO.add_event_detect(12, GPIO.BOTH, callback=my_callback)

try:
    while True:
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()

GPIO.cleanup()


# def Start_Code():
#     running = 0
#     GPIO.output(40,False)
#     GPIO.output(38,False)
#     GPIO.output(36,False)
#     while True:
#         input_state = GPIO.input(12)
#         if input_state == False and running == 0:
#             print('On')
#             blink_proc = subprocess.Popen("/home/pi/Self_Driving_Car_Project/SDRC_Project/SDRC_Project/Python_Starter_Code/Blink_Tri.sh", shell=True, preexec_fn=os.setsid)
#             time.sleep(0.2)
#             running = 1
#         while input_state == True:
#             if running == 1:
#                 print('Off')
#                 os.killpg(blink_proc.pid, signal.SIGTERM)
#                 blink_proc = None
#
#                 GPIO.output(40,False)
#                 GPIO.output(38,False)
#                 GPIO.output(36,False)
#                 running = 0
#             else:
#                 input_state = GPIO.input(12)
#                 GPIO.output(40,True)
#                 time.sleep(0.5)
#                 input_state = GPIO.input(12)
#                 GPIO.output(40,False)
#                 time.sleep(0.5)
#
#     return;
