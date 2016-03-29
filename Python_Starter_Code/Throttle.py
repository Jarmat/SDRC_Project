import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    pwm_29 = GPIO.PWM(29, 100)
    pwm_31 = GPIO.PWM(31, 100)
    pwm_29.start(0)
    pwm_31.start(0)
    GPIO.output(33, True)

def Forward(ts,velocity):
    pwm_31.ChangeDutyCycle(velocity)
    time.sleep(ts)


def Reverse(ts,velocity):
    pwm_29.ChangeDutyCycle(velocity)
    time.sleep(ts)

def Stop(ts):
    GPIO.output(33, False)
    pwm_29.ChangeDutyCycle(0)
    pwm_31.ChangeDutyCycle(0)

def Clean():
    pwm_29.stop()
    pwm_31.stop()
    GPIO.cleanup()

init()

for x in range (5):
    Forward(0.2,20)

Stop(0.2)

for x in range(5):
    Reverse(0.2,10)

Clean()
