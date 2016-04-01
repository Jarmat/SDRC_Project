import RPi.GPIO as GPIO
import time

from Move_and_Sense_Script import Launch_Car

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use
GPIO.setup(38, GPIO.OUT)
GPIO.setup(36, GPIO.OUT)

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

def Launch_Car():

    print("Start Car...")

    return;

Blink_Tri()
Launch_Car()
