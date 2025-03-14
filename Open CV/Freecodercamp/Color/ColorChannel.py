import cv2 as cv
import numpy as np

img = cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg")
cv.imshow('Gateway of India',img)

b,g,r = cv.split(img)
cv.imshow('Blue',b)
cv.imshow('Green',g)
cv.imshow('Red',r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blank = np.zeros(img.shape[:2],dtype='uint8')

blue = cv.merge([b,blank,blank])    
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue 1',blue)
cv.imshow('Green 1',green)
cv.imshow('Red 1',red)

blue_green = cv.merge([b,g,blank])    
green_red = cv.merge([blank,g,r])
red_blue = cv.merge([b,blank,r])

cv.imshow('Blue Green',blue_green)
cv.imshow('Green Red',green_red)
cv.imshow('Red Blue',red_blue)

cv.imshow('BGR',cv.merge([b,g,r]))
cv.imshow('GRB',cv.merge([g,r,b]))
cv.imshow('RBG',cv.merge([r,b,g]))

cv.waitKey(0)