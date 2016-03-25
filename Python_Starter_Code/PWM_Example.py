import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.

pwm_obj = GPIO.PWM(13, 400) #Sets pin 13 as a PWM output at 400 Hz.

pwm_obj.start(100) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).

pwm_obj.ChangeDutyCycle(50) #Changes the Duty cycle to 50 (obviously).
