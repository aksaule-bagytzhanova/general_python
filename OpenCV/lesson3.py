import cv2

img1 = cv2.imread('pic/op.jpg')
img2 = cv2.imread('pic/logo.png')

r1 = cv2.resize(img1, (720, 720))
r2 = cv2.resize(img2, (720, 720))

#s = cv2.add(r1, r2)
#s = cv2.subtract(r2,r1)
s = cv2.addWeighted(r1,1,r2,0.5,0)

cv2.imshow('add', s)
cv2.waitKey(0)
cv2.destroyAllWindows()