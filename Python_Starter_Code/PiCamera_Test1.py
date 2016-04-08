import time
import picamera
from Laser import Laser_On, Laser_Off

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        # camera.led = False
        # camera.shutter_speed = 250
        camera.resolution = (640, 480)
        camera.start_preview()
        # Camera warm-up time
        time.sleep(2)


        try:
            for x in range(10):
                start = time.time()
                Laser_On()
                camera.capture(output, format='rgb')
                Laser_Off()
                stop = time.time()
                print stop-start
        except KeyboardInterrupt:
            print 'Quit'
            Laser_Off()
