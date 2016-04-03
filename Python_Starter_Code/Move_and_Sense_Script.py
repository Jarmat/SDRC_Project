import RPi.GPIO as GPIO
import time

from Throttle import Forward, Reverse, Stop, Throttle_Init
from UltraSonic import DistanceSense, Ultrasonic_Init
from Turn import TurnRight, TurnLeft, TurnStraight, Turn_Init, Turn_Clean

def Launch_Car():
    GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
    GPIO.setup(29, GPIO.OUT)
    GPIO.setup(31, GPIO.OUT)
    GPIO.setup(33, GPIO.OUT)
    pwm29 = GPIO.PWM(29, 100)
    pwm31 = GPIO.PWM(31, 100)
    pwm29.start(0)
    pwm31.start(0)
    GPIO.output(33, True)
    GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.
    GPIO.setup(12, GPIO.OUT)
    pwm_12 = GPIO.PWM(12, 50) #Sets pin 18 as a PWM output at 50 Hz.
    pwm_12.start(0) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).

    ts = 0.02

    while True:

        distance = DistanceSense('cm')
        print distance

        if distance == None:
            print "Error detected, stopping code."
            break

        steps = 0

        while distance < 5:
            steps += 1
            Stop(ts)
            TurnRight(ts)
            Reverse(0.5,15)
            TurnLeft(ts)
            Forward(0.5,15)
            Stop(ts)
            TurnStraight(ts)
            distance = DistanceSense('cm')
            if steps > 4:
                print "I'm stuck!  Exiting code..."
                break

        if steps > 4:
            break

        while distance > 30:
            Forward(ts, 20)
            distance = DistanceSense('cm')


    pwm29.stop()
    pwm31.stop()
    pwm_12.stop()
    GPIO.cleanup()

    return;

Launch_Car()
