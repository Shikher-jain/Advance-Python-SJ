import cv2 as cv

img = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg")
cv.imshow('Gateway of India',img)

bitwise_and = cv.bitwise_and(img,img)
cv.imshow('Bitwise AND',bitwise_and)

bitwise_or = cv.bitwise_or(img,img)
cv.imshow('Bitwise OR',bitwise_or)

bitwise_xor = cv.bitwise_xor(img,img)
cv.imshow('Bitwise X-OR',bitwise_xor)

bitwise_not = cv.bitwise_not(img)
cv.imshow('Bitwise NOT',bitwise_not)

cv.waitKey(0)