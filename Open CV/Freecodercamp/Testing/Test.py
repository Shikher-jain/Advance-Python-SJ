import cv2 as cv
import numpy as np

img=[
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]]]

# cv.imshow("IMAGE", img)

img1 = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg", 1)
img0 = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg", 0)
imgn1= cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg", -1)

blank = np.zeros(img1.shape[:2],dtype='uint8')
blank2 = np.zeros(img1.shape[:2],np.uint8)

cv.imshow('Blank',blank)
cv.imshow('Blank 2',blank2)

gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
# canny = cv.Canny(gray, 125, 175)
# cv.imshow('Original 0',img0)
# cv.imshow('Original 1',img1)
# cv.imshow('RGB',rgb)

# cv.imshow('Original n1',imgn1)
# cv.imshow('Gray',gray)
cv.waitKey(0)