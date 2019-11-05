# Example of camera calibration using chess board pattern
# Based on code by Alexander Mordvintsev & Abid K.:
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_calib3d/py_calibration/py_calibration.html
# Includes some nice (but ultimately unecessary) visual feedback while working

import numpy as np
import cv2
import glob

# Parameters
# distortedImage is the image that will be undistorted (done on an image-by-image basis)
calibrationImgPath = "img/calibration/side/*.jpg"
distortedImage = "img/testing/side.jpg"


# Part 1: Mark the points on the checkerboard in each image
# At least 20 images should be used

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
# 6x4 chess board (that's 6x4 crossing points), with square side length 38mm
objp = np.zeros((4*6,3), np.float32)
objp[:,:2] = np.mgrid[0:6,0:4].T.reshape(-1,2)*38 # 38 mm square size

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

images = glob.glob(calibrationImgPath)

for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv2.findChessboardCorners(gray, (6,4),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (6,4), corners2,ret)
        cv2.imshow('img',img)
        cv2.waitKey(50)

cv2.destroyAllWindows()



# Part 2: Calibrate camera
# Based on the object and image points found above,
# find the camera matrix, distortion coefficients, rotation and translation vectors etc.
# TODO: These values should be attained for each camera at the beginning of the main program.
#       That way, we can undistort images as they're taken. (It's done on an image-by-image basis)
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

# Take an image to compare before-and-after undistortion
distImg = cv2.imread(distortedImage)
h,  w = distImg.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx,dist,(w,h),1,(w,h))



# Part 3: Undistortion
undistImg = cv2.undistort(distImg, mtx, dist, None, newcameramtx)

# crop the image
x,y,w,h = roi
dst = undistImg[y:y+h, x:x+w]
#cv2.imwrite('calibresult.png',dst)
cv2.imshow("Original image", distImg)
cv2.imshow("After undistortion", undistImg)
cv2.waitKey()


# Part 4 (optional): Testing re-projection error
# This part checks how reliable the parameters we've found are
# The closer mean error is to zero, the better
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv2.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv2.norm(imgpoints[i],imgpoints2, cv2.NORM_L2)/len(imgpoints2)
    mean_error += error

print("Total error: ", mean_error/len(objpoints))