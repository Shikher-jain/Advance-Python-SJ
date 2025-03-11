import cv2

img = cv2.imread('F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Freecodercamp\gatewayOfIndia.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

X = cv2.Sobel(gray, cv2.CV_64F, 1, 0)
Y = cv2.Sobel(gray, cv2.CV_64F, 0, 1)

XY = cv2.bitwise_or(X, Y)


cv2.imshow('Sobel Edge Detection X', X)
cv2.imshow('Sobel Edge Detection Y', Y)
cv2.imshow('Sobel Edge Detection XY', XY)
cv2.imshow('Sobel Edge Detection XY INV', cv2.bitwise_not(XY))

cv2.waitKey(0)
cv2.destroyAllWindows()