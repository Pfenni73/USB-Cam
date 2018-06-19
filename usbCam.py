class UsbCam():
    import os
    import datetime
    import time
    
    def __init__(self, usbCam_picPath):
        self.picPath = usbCam_picPath
        
    def set_PicPath(self, usbCam_picPath):
        self.picPath = usbCam_picPath
        
    def takeSinglePic(self, usbCam_PicName):
        self.os.system ("fswebcam -d/dev/video0 -r640x480 {}/{}{}.jpeg".format(self.picPath, usbCam_PicName, self.datetime.datetime.now().isoformat()));
        
    def takeSeriePic(self, usbCam_nrOfPics):
        for nr in range(0,usbCam_nrOfPics):
            self.takeSinglePic("Serie");
            self.time.sleep(1);