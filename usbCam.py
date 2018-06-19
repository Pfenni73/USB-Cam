class UsbCam():
    import os
    import datetime
    
    def __init__(self, usbCam_picPath):
        self.picPath = usbCam_picPath
        
    def set_PicPath(self, usbCam_picPath):
        self.picPath = usbCam_picPath
        
    def takeSinglePic(self):
        self.os.system ("fswebcam -d/dev/video0 -r640x480 /home/pi/Documents/testbild{}.jpeg".format(self.datetime.datetime.now().isoformat()));