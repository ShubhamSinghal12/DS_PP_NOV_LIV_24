import cv2


img = cv2.imread('dog-Copy1.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('Dog Image',img)
cv2.imshow('Gray Dog Image',gray)

cv2.waitKey(5000)
cv2.destroyAllWindows()