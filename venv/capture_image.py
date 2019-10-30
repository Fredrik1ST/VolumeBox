import cv2

video_capture = cv2.VideoCapture(1)
# Check success
if not video_capture.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = video_capture.read()
cv2.imshow("Window", frame)
cv2.waitKey()
cv2.destroyAllWindows()
# Close device
video_capture.release()

