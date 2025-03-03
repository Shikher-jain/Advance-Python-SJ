import cv2 as cv
import numpy as np

img = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg")
cv.imshow('Gateway of India',img)

# Averaging
avgerage_Blur = cv.blur(img,(7,7))
cv.imshow('Avgerage Blur',avgerage_Blur)

# Gaussian Blur
Gaussian_Blur = cv.GaussianBlur(img,(7,7), 0)
cv.imshow('Gaussian Blur',Gaussian_Blur)

# Median Blur
median = cv.medianBlur(img,7)
cv.imshow('Median',median)

# Bilateral
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('Bilateral',bilateral)

cv.waitKey(0)