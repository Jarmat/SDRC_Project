import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD) # select the GPIO numbering scheme to use.

pwm_obj = GPIO.PWM(18, 50) #Sets pin 18 as a PWM output at 50 Hz.

pwm_obj.start(100) #Starts the PWM with a duty cycle of 100 (Duty cycle ranges between 0 and 10).

pwm_obj.ChangeDutyCycle(50) #Changes the Duty cycle to 50 (obviously).

# Use ChangeDutyCycle() to control the position of the servo in pwm mode.
