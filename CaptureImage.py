import cv2

def captureImage(fromAngle):
    if fromAngle is "side":
        imgOutputPath = "img/side.jpg"
        cameraID = 1;
    elif fromAngle is "top":
        imgOutputPath = "img/top.jpg"
        cameraID = 2;
    else:
        imgOutputPath = "img/accidental.jpg"
        cameraID = 0;

    # Function to change camera resolution
    def change_res(width, height):
        cap.set(3, width)
        cap.set(4, height)

    # Set up camera object
    cap = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)
    change_res(960, 720)

    # Check success
    if not cap.isOpened():
        raise Exception("Could not open video device")
    # Read picture. ret === True on success
    ret, frame = cap.read()
    cv2.imwrite(imgOutputPath, frame)

    cv2.imshow("Captured image", frame)
    cv2.waitKey()
    cv2.destroyAllWindows()
    # Close device
    cap.release()