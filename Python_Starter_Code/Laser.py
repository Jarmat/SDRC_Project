import RPi.GPIO as GPIO
import time


def Laser_On(ts):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)

    GPIO.output(13, True)
    time.sleep(ts)
    GPIO.output(13,False)

    return;


while True:
    Laser_On(0.02)
    time.sleep(0.2)
