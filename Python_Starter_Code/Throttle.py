import RPi.GPIO as GPIO
import time

#def initialize():
GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
pwm29 = GPIO.PWM(29, 100)
pwm31 = GPIO.PWM(31, 100)
pwm29.start(0)
pwm31.start(0)
GPIO.output(33, True)
 #   return;

def Forward(ts,velocity):
    pwm31.ChangeDutyCycle(velocity)
    time.sleep(ts)
    return;



def Reverse(ts,velocity):
    pwm29.ChangeDutyCycle(velocity)
    time.sleep(ts)
    return;

def Stop(ts):
    GPIO.output(33, False)
    pwm29.ChangeDutyCycle(0)
    pwm31.ChangeDutyCycle(0)
    return;

def Clean():
    pwm29.stop()
    pwm31.stop()
    GPIO.cleanup()
    return;


for x in range (5):
    Forward(0.2,20)

Stop(0.2)

for x in range(5):
    Reverse(0.2,10)

Clean()
