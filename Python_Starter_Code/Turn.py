import RPi.GPIO as GPIO
import time

def Turn_Init():
    GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
    GPIO.setup(12, GPIO.OUT)
    pwm_12 = GPIO.PWM(12, 50) #Sets pin 18 as a PWM output at 50 Hz.
    pwm_12.start(0) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).
    return;

def TurnLeft(pwm_12,ts):
    pwm_12.ChangeDutyCycle(12)
    time.sleep(ts)

    return;

def TurnRight(pwm_12,ts):
    pwm_12.ChangeDutyCycle(1.5)
    time.sleep(ts)

    return;

def TurnStraight(pwm_12,ts):
    pwm_12.ChangeDutyCycle(9)
    time.sleep(ts)

    return;

def Turn_Clean():
    pwm_12.stop()
    # GPIO.cleanup()

    return;

# TurnLeft(2)
# TurnStraight(2)
# TurnRight(2)
# TurnStraight(2)
#
#
# Clean()
