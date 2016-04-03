import RPi.GPIO as GPIO
import time

def Ultrasonic_Init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35, GPIO.IN)
    GPIO.setup(37, GPIO.OUT)
    return;

def DistanceSense(units):

    print units

    GPIO.output(35, False)

    while GPIO.input(37) == 0:
        nosig = time.time()

    while GPIO.input(37) == 1:
        sig = time.time()

    tl = sig - nosig

    if units == 'cm':
        distance = tl/0.000058
        print 'Distancs is ', distance
    elif units == 'in':
        distance = tl/0.000148
        print 'Distancs is ', distance
    else:
        print('Use either cm or in for units.')
        distance = None

    return distance;

Ultrasonic_Init()
DistanceSense('cm')
