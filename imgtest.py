import cv2

img = cv2.imread('pic1.jpg')
cv2.imshow('img', img)

cv2.circle(img, (121, 126), 4, color=(112, 25, 25), thickness=-1)
cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
