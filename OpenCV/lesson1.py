import cv2
import numpy as np

#IMAGE
# img = cv2.imread("pic/logo.png", 1)
# cv2.namedWindow("image_logo", cv2.WINDOW_NORMAL)
# cv2.imshow("image_logo", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


#VIDEO camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break



#VIDEO
cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()
    cv2.imshow("video", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()