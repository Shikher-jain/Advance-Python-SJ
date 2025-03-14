import cv2 as cv
import numpy as np

img = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/Cats.jpeg")
cv.imshow('Cats',img)

blank = np.zeros(img.shape[:2],dtype='uint8')
circle = cv.circle(blank.copy(),(img.shape[1]//2,img.shape[0]//2),100,255,-1)
rectangle = cv.rectangle(blank.copy(),(30,90),(370,370),255,-1)

# Bitwise AND
Shape = cv.bitwise_and(circle,rectangle)
cv.imshow('Bitwise AND',Shape)

masked = cv.bitwise_and(img,img,mask=Shape)
cv.imshow('Masked Image 1',masked)

cv.waitKey(0)