import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
GPIO.setup(29, GPIO.OUT)
GPIO.setup(31, GPIO.OUT)
GPIO.setup(33, GPIO.OUT)
pwm29 = GPIO.PWM(29, 100)
pwm31 = GPIO.PWM(31, 100)
pwm29.start(0)
pwm31.start(0)
GPIO.output(33, True)

def Forward(pwm29,ts,velocity):
    pwm29.ChangeDutyCycle(velocity)
    time.sleep(ts)
    return;

def Reverse(pwm31,ts,velocity):
    pwm31.ChangeDutyCycle(velocity)
    time.sleep(ts)
    return;

def Stop(pwm29,pwm31,ts):
    pwm29.ChangeDutyCycle(0)
    pwm31.ChangeDutyCycle(0)
    time.sleep(ts)
    return;

def Throttle_Clean():
    pwm29.stop()
    pwm31.stop()
    # GPIO.cleanup()
    return;


# for x in range (5):
#     Forward(1,20)
#
# Stop(1)
#
# for x in range(5):
#     Reverse(1,20)
#
# pwm29.stop()
# pwm31.stop()
# GPIO.cleanup()
