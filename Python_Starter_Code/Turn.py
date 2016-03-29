import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
GPIO.setup(12, GPIO.OUT)
pwm_obj = GPIO.PWM(12, 50) #Sets pin 18 as a PWM output at 50 Hz.
pwm_obj.start(0) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).

def TurnLeft(ts):
    pwm_obj.ChangeDutyCycle(12)
    time.sleep(ts)

    return;

def TurnRight(ts):
    pwm_obj.ChangeDutyCycle(1.5)
    time.sleep(ts)

    return;

def TurnStraight(ts):
    pwm_obj.ChangeDutyCycle(1.5)

def Clean():
    pwm_obj.stop()
    GPIO.cleanup()


TurnStraight(2)
TurnLeft(2)
TurnStraight(2)
TurnRight(2)
TurnStraight(2)

Clean()
