import cv2
import numpy as np

video = cv2.VideoCapture("./green_screen.mp4")
image = cv2.imread("./autumn.webp")

while True:
    ret, frame = video.read()
    if type(frame) == type(None):
        print("Video Ended")
        break
    frame = cv2.resize(frame, (640, 480))
    image = cv2.resize(image, (640, 480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_g = np.array([32, 94, 132])
    u_g = np.array([179, 255, 255])

    mask = cv2.inRange(hsv, l_g, u_g)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = frame - res
    green_screen = np.where(f == 0, image, f)
    cv2.imshow("Processed Video", green_screen)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
