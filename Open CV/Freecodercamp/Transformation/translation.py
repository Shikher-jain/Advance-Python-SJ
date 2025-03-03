import cv2
import numpy as np

img=cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')

if img is None:
    print("Error: Image not found!")
    exit()

cv2.imshow('Original',img)

def translate(img,x,y):
    Mat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv2.warpAffine(img,Mat,dimensions)

for i,j in [(100,100),(100,-100),(-100,-100),(-100,100)]:
    translated = translate(img,i,j)
    cv2.imshow(f'Translated {i} {j}',translated)

# translated = translate(img,100,100)
# cv2.imshow('Translated',translated)

cv2.waitKey(0)