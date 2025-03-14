import cv2 as cv
import numpy as np

img = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg")
cv.imshow('Gateway of India',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

canny = cv.Canny(blur,125,175)
cv.imshow('Canny Edges',canny)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('Blank Image',blank)

contours, hierarcies =cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found simple list')

contours, hierarcies =cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found none list')

contours, hierarcies =cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found simple tree ')

contours, hierarcies =cv.findContours(canny,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found none tree ')

contours, hierarcies =cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found simple external ')

contours, hierarcies =cv.findContours(canny,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found none external ')


cv.drawContours(blank,contours,-1,(0,0,255),1)
cv.imshow('Contours Drawn',blank)

ret,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)


cv.waitKey(0)