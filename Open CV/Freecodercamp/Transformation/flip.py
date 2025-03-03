import cv2
import numpy as np

img=cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')
cv2.imshow('Original',img)

def flip(img,flipCode):
    return cv2.flip(img,flipCode)

for i in [0,1,-1]:
    flipped=flip(img,i)
    cv2.imshow(f'Flipped {i}',flipped)
# flipped=flip(img,0)
# cv2.imshow('Flipped 0',flipped)

cv2.waitKey(0)