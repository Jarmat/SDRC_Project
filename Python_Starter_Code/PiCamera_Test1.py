import time
import picamera
from Laser import Laser_On, Laser_Off

with picamera.PiCamera() as camera:
    # camera.led = False
    camera.shutter_speed = 250
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)


    try:
        while True:
            start = time.time()
            Laser_On()
            camera.capture('foo.jpg')
            Laser_Off()
            stop = time.time()
            print stop-start
    except KeyboardInterrupt:
        print 'Quit'
        Laser_Off()
