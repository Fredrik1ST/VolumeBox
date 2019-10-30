# For running small stubs of code when needed

import cv2

# Display some image from a folder around here
img = cv2.imread("img/calibration/side/side (1).jpg")
cv2.imshow("Window", img)
cv2.waitKey()
cv2.destroyAllWindows()