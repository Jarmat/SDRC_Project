import RPi.GPIO as GPIO
import time
import Tkinter as tk

from Throttle import Forward, Reverse, Stop
from UltraSonic import DistanceSense
from Turn import TurnRight, TurnLeft, TurnStraight, Turn_Clean

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

def key_input(event):

    print 'Key:', event.char

    key_press = event.char
    ts = 0.03
    velocity = 80

    if key_press.lower() == w:
        Forward(pwm29,ts, velocity)
    elif key_press.lower() == s:
        Reverse(pwm31,ts, velocity)
    else:
        Stop(pwm29,pwm31,ts)

    if key_press.lower() == a:
        TurnLeft(pwm12,ts)
    elif key_press.lower() == a:
            TurnLeft(pwm12,ts)
    else:
        TurnStraight(pwm_12,ts)


command = tk.TK()
command.blind('<KeyPress>', key_input)
command.mainloop()
