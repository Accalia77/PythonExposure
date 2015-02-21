import time
import picamera

with picamera.PiCamera() as camera:
	filename = "storage/images/" + str(time.time()) + ".jpg"	
	camera.hflip = True
	camera.vflip = True
	camera.capture(filename)
