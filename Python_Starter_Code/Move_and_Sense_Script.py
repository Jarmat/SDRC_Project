import RPi.GPIO as GPIO
import time

from Throttle import Forward, Reverse, Stop, Throttle_Init
from UltraSonic import DistanceSense, Ultrasonic_Initgit
from Turn import TurnRight, TurnLeft, TurnStraight, Turn_Init, Turn_Clean

def Launch_Car():
    Throttle_Init()
    Ultrasonic_Init()
    Turn_Init()
    ts = 0.2

    while True:

        distance = DistanceSense('cm')

        if distance == None:
            print "Error detected, stopping code."
            break

        steps = 0

        while distance < 30:
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



    Throttle_Clean()
    Turn_Clean()
    GPIO.cleanup()

    return;
