import cv2

img = cv2.imread('F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Freecodercamp\gatewayOfIndia.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
cv2.imshow('Laplacian Edge Detection ', laplacian)
cv2.imshow('Laplacian Edge Detection INV', cv2.bitwise_not(laplacian))

laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow('Laplacian Edge Detection 2', laplacian)
cv2.imshow('Laplacian Edge Detection 2 INV', cv2.bitwise_not(laplacian))

cv2.waitKey(0)
cv2.destroyAllWindows()