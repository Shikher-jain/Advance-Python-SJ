import cv2
import numpy as np

img=cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')
cv2.imshow('Original',img)

def crop(img,x,y,w,h):
    return img[y:y+h,x:x+w]

for i,j,k,l in [(0,0,200,200),(100,100,200,200),(200,200,200,200),(300,300,200,200)]:
    cropped=crop(img,i,j,k,l)
    cv2.imshow(f'Cropped {i} {j} {k} {l}',cropped)

# cropped=crop(img,100,100,200,200)
# cv2.imshow('Cropped',cropped)

cv2.waitKey(0)