import CaptureImage, UndistortImage, MeasureObjectSize, CalculateVolume
import cv2
import numpy as np

"""
A quick rundown of how the volume box works:
    - User places reference object to the left of what is to be measured.
    - The cameras take one picture each.
    - Camera calibration is performed for each camera. Camera matrices are used to undistort the images.
    - The object is extracted and measured in X and Y directions.
    - Measurements are combined to calculate volume.
    
    Change the filename paths in the functions below to use different sets of images.
    Newly captured images are saved as "img/side.jpg" or "img/top.jpg". Test images are in their own folder.
    Undistorted images are saved as "img/undistortedSide.jpg" or "img/undistortedTop.jpg".
    
"""

# TODO: Uncomment and run live from start to finish. Thus far only the set of test images have been used.
#CaptureImage.captureImage("WRITE EITHER side OR top IN HERE")
#UndistortImage.undistortImage("img/testing/side.jpg", "side")
#UndistortImage.undistortImage("img/testing/top.jpg", "top")
sideX, sideY = MeasureObjectSize.measureObjectSize("img/testing/side.jpg", "side")
topX, topY = MeasureObjectSize.measureObjectSize("img/testing/top.jpg", "top")
# Volume in cubic millimeters
volume = CalculateVolume.calculateVolume("cube", sideX, sideY, topX, topY)

# Show the user the estimated volume with some fancy graphics
image = np.zeros((100,1000,4),np.uint8)
text = "Estimated volume = %f cm^3" % (volume/1000)
print(text)
cv2.putText(image, text, (10,50),cv2.FONT_HERSHEY_PLAIN,3,(70,230,130,255), 3)
cv2.imshow('Result', image)
cv2.waitKey()
cv2.destroyAllWindows()
