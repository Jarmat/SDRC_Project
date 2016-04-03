import RPi.GPIO as GPIO
import time

def Ultrasonic_Init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35, GPIO.IN)
    GPIO.setup(37, GPIO.OUT)
    return;

def DistanceSense(units):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(35, GPIO.IN)
    GPIO.setup(37, GPIO.OUT)

    time.sleep(0.02)

    GPIO.output(37, True)

    time.sleep(0.00001)

    GPIO.output(37, False)

    while GPIO.input(35) == 0:
        nosig = time.time()

    while GPIO.input(35) == 1:
        sig = time.time()

    tl = sig - nosig

    if units == 'cm':
        distance = tl/0.000058
    elif units == 'in':
        distance = tl/0.000148
    else:
        print('Use either cm or in for units.')
        distance = None

    return distance;

print DistanceSense('cm')
GPIO.cleanup()
