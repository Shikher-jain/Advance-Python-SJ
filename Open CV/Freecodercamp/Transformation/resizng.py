import cv2
import numpy as np

img=cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')
cv2.imshow('Original',img)

def resizng(img,scale=0.75):
    width=int(img.shape[1]*scale)   
    height=int(img.shape[0]*scale)
    dimensions=(width,height)
    return cv2.resize(img,dimensions,interpolation=cv2.INTER_AREA)

for i in [0.5,0.75,1.5,2]:
    resized=resizng(img,i)
    cv2.imshow(f'Resized {i}',resized)

cv2.waitKey(0)