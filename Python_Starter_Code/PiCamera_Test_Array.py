import time
import picamera
import picamera.array

with picamera.PiCamera() as camera:
    with picamera.array.PiRGBArray(camera) as output:
        camera.start_preview()
        time.sleep(2)
        camera.resolution = (640, 480)
        camera.capture(output, format='rgb')
        print('Captured %dx%d image' % (
                output.array.shape[1], output.array.shape[0]))
