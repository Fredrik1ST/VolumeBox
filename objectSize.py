# import the necessary packages
from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2


def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

inputImgPath = "img/testing/side.jpg"
refObjectWidth = 10 # Width of reference object in millimeters

# PART 1 : Extracting objects from image #
# Based on objects being some hue of red #

# load the image, create a mask to filter out the ROI / objects
img = cv2.imread(inputImgPath)
hsvImg = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# Work in progress: finding a proper color threshold
lowerRed = np.array([0,0,0])
upperRed = np.array([50,150,50])
mask = cv2.inRange(hsvImg, lowerRed, upperRed)
maskedImg = cv2.bitwise_and(img, img, mask=mask) # Runs the mask over

#gray = cv2.cvtColor(hsvImg, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(hsvImg, (7, 7), 0)
cv2.imshow("Input image", img)
cv2.imshow("HSV", hsvImg)
cv2.waitKey()
cv2.destroyAllWindows()