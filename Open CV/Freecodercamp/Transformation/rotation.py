import cv2 as cv
import numpy as np

def rotation(img, angle,rotPoint=None):
    (height,width)=img.shape[:2]
    if rotPoint is None:
        rotPoint=(width//2,height//2)
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1.0)   
    dimensions=(width,height)
    return cv.warpAffine(img,rotMat,dimensions)

img=cv.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')
cv.imshow('Original',img)

for i in range(0,360,45):
    rotated=rotation(img,i)
    cv.imshow(f'Rotated 1 {i}',rotated)

rotated=rotation(img,0)
for i in range(0,360,45):
    rotated=rotation(rotated,i)
    cv.imshow(f'Rotated 2 {i}',rotated)


# rotated=rotation(img,45)
# cv.imshow('Rotated',rotated)
# rotated2=rotation(rotated,45)
# cv.imshow('Rotated2',rotated2)
# rotated3=rotation(rotated2,45)
# cv.imshow('Rotated2',rotated3)
# rotated4=rotation(rotated3,45)
# cv.imshow('Rotated3',rotated4)

cv.waitKey(0)