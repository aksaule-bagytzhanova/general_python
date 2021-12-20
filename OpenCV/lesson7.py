import cv2
import numpy as np
import time

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read(0)
#     cv2.imshow("frame", frame)
#
#     #обычное сглаживание
#     blur = cv2.blur(frame, (5,5))
#     # blur = cv2.blur(frame, (111,111))
#
#     cv2.imshow("blur", blur)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()

# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read(0)
#     cv2.imshow("frame", frame)
#
#     #сглаживание по гаусу
#     blur = cv2.GaussianBlur(frame, (5,5), 0)
#
#     cv2.imshow("blur", blur)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()


#Биутральное размытие
# cap = cv2.VideoCapture(0)
#
# while True:
#     ret, frame = cap.read(0)
#     cv2.imshow("frame", frame)
#
#     #Биутральное размытие
#     blur = cv2.bilateralFilter(frame, 21, 75, 75)
#
#     cv2.imshow("blur", blur)
#
#     k = cv2.waitKey(1) & 0xFF
#     if k == 27:
#         break
#
# cv2.destroyAllWindows()
from cv2 import bilateralFilter


def nothing(x):
    pass

kernel = np.ones((5,5), np.uint8)
cap = cv2.VideoCapture(0)
cv2.namedWindow('track')

cv2.createTrackbar("HL", "track", 0, 180, nothing)
cv2.createTrackbar("SL", "track", 0, 255, nothing)
cv2.createTrackbar("VL", "track", 0, 255, nothing)

cv2.createTrackbar("H", "track", 0, 180, nothing)
cv2.createTrackbar("S", "track", 0, 255, nothing)
cv2.createTrackbar("V", "track", 0, 255, nothing)

while True:
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hl = cv2.getTrackbarPos("HL", "track")
    sl = cv2.getTrackbarPos("SL", "track")
    vl = cv2.getTrackbarPos("VL", "track")

    h = cv2.getTrackbarPos("H", "track")
    s = cv2.getTrackbarPos("S", "track")
    v = cv2.getTrackbarPos("V", "track")

    lower = np.array([hl,sl,vl])
    upper = np.array([h,s,v])
    frame = bilateralFilter(frame, 9, 75, 75)
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    edge = cv2.Canny(mask, 100, 200)

    countours, h = cv2.findContours(edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
    countours = sorted(countours, key = cv2.contourArea, reverse=True)

    try:
        cv2.drawContours(frame, [countours[0]],-1, (255,0,0),5)
    except Exception:
        print()

    cv2.imshow("mask", mask)
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask, kernel, iterations=1)
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    cv2.imshow("close", closing)
    cv2.imshow("frame", frame)


    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()