import time
import picamera
from Laser import Laser_On, Laser_Off

with picamera.PiCamera() as camera:
    # camera.led = False
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)

    Laser_On()
    camera.capture('foo.jpg')
    Laser_Off()
