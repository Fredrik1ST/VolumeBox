import cv2

# Function to change camera resolution
def change_res(width, height):
    cap.set(3, width)
    cap.set(4, height)

imgOutputName = "side.jpg" # Name of image saved
topCamera = 0; # ID of top camera
sideCamera = 1; # ID of side camera

# Set up camera object
cap = cv2.VideoCapture(1)
change_res(960, 720)

# Check success
if not cap.isOpened():
    raise Exception("Could not open video device")
# Read picture. ret === True on success
ret, frame = cap.read()
cv2.imwrite(imgOutputName, frame)

cv2.imshow("Captured image", frame)
cv2.waitKey()
cv2.destroyAllWindows()
# Close device
cap.release()