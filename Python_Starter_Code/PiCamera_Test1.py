import time
import picamera
import picamera.array
from Laser import Laser_On, Laser_Off

with picamera.PiCamera() as camera:
    # with picamera.array.PiRGBArray(camera) as output:
    # camera.led = False
    camera.shutter_speed = 1000
    camera.resolution = (640, 480)
    camera.start_preview()
    # Camera warm-up time
    time.sleep(2)


    try:
        start = time.time()
        for x in range(10):

            Laser_On()
            # camera.capture(output, format='rgb')
            camera.capture('foo.jpg')
            Laser_Off()
            stop = time.time()

            # output.truncate(0)
        stop = time.time()
        print (stop-start)/10
    except KeyboardInterrupt:
        print 'Quit'
        Laser_Off()
