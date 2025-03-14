import cv2 as cv
import numpy as np

blank=np.zeros((400,400),dtype='uint8')
circle =cv.circle(blank.copy(),(200,200),200,255,-1)
rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)

cv.imshow('Circle',circle)
cv.imshow('Rectangle',rectangle)

# Bitwise operations
bitwise_and = cv.bitwise_and(circle,rectangle)
cv.imshow('Bitwise AND',bitwise_and)

# Bitwise OR
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('Bitwise OR',bitwise_or)

# Bitwise XOR
bitwise_xor = cv.bitwise_xor(circle,rectangle)
cv.imshow('Bitwise X-OR',bitwise_xor)

# Bitwise NOT
bitwise_notC = cv.bitwise_not(circle)
cv.imshow('Bitwise NOT C',bitwise_notC)

bitwise_notR = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT R',bitwise_notR)


cv.waitKey(0)