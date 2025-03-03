import cv2

img=[
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]],
 [[255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [255 ,255 ,255], [251 ,251 ,251], [228 ,228 ,229]]]

cv2.imshow("IMAGE", img)



import cv2 as cv

img1 = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg", 1)
img0 = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg", 0)
imgn1= cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg", -1)


gray = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)
rgb = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
# canny = cv.Canny(gray, 125, 175)
cv.imshow('Original 0',img0)
cv.imshow('Original 1',img1)
cv.imshow('RGB',rgb)

cv.imshow('Original n1',imgn1)
cv.imshow('Gray',gray)
cv.waitKey(0)