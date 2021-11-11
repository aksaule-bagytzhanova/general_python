import cv2
import numpy as np

img = np.zeros((900,900,3), np.uint8)

img = cv2.line(img,(10,10),(720,640),(140,160,180),1)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()