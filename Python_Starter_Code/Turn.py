import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.

GPIO.setup(18, GPIO.OUT)

pwm_obj = GPIO.PWM(18, 50) #Sets pin 18 as a PWM output at 50 Hz.

pwm_obj.start(100) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).

pwm_obj.ChangeDutyCycle(50) #Changes the Duty cycle to 50 (obviously).

# Use ChangeDutyCycle() to control the position of the servo in pwm mode.

def TurnLeft(ts):
    pwm_obj.ChangeDutyCycle(12)
    time.sleep(ts)

    return;

def TurnRight(ts):
    pwm_obj.ChangeDutyCycle(4)
    time.sleep(ts)

    return;

def TurnStraight(ts):
    pwm_obj.ChangeDutyCycle(8.5)

TunrLeft(0.2)
TurnRight(0.2)
