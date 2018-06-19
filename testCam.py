from usbCam import UsbCam

cam = UsbCam("/home/pi/Pictures");
#cam.takeSinglePic("Bild");
cam.takeSeriePic(4);