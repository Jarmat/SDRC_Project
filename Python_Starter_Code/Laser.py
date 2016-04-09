import RPi.GPIO as GPIO
import time


def Laser_Blink(ts):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)

    GPIO.output(13, True)
    time.sleep(ts)
    GPIO.output(13,False)
    GPIO.cleanup()
    return;

def Laser_On():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(13, GPIO.OUT)

    GPIO.output(13, True)

def Laser_Off():
    GPIO.output(13,False)
    GPIO.cleanup()


try:
    while True:
        Laser_Blink(0.01)
        time.sleep(0.2)
except KeyboardInterrupt:
    print 'Quit'
    GPIO.cleanup()
