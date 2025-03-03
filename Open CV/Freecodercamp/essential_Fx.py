# 5 Essential Functions in OpenCV

import cv2 as cv

img=cv.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg')
# cv.imshow('Gateway of India',img)


# Resize the image (zoom in)
scale_factor=1.75
Img = cv.resize(img, None, fx=scale_factor, fy=scale_factor, interpolation=cv.INTER_LINEAR)
# cv.imshow('Zoom Img', Img)


# 1. Converting Images to Grayscale
# cv.imshow('Gray Image', cv.cvtColor(img, cv.COLOR_BGR2GRAY))
# cv.imshow('Gray Zoom Image', cv.cvtColor(Img, cv.COLOR_BGR2GRAY))

# 2. Blurring Images
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur Image', blur)
# cv.imshow('Blur Zoom Image', cv.GaussianBlur(Img, (7,7), cv.BORDER_DEFAULT))


# 3. Canny Edge Detection
canny = cv.Canny(img, 125, 175)
blurCanny = cv.Canny(blur, 125, 175)
Cannycanny = cv.Canny(canny, 125, 175)
# cv.imshow('Canny Image', canny)
# cv.imshow('Blur Canny Image', blurCanny)
# cv.imshow('Canny Canny Image', Cannycanny)

# 4. Dilating an Image

#   - Dilation
dilated = cv.dilate(blurCanny, (7,7), iterations=3)
# cv.imshow('Dilated Image', dilated)

#   - Erosion 
eroded = cv.erode(dilated, (7,7), iterations=3)
# cv.imshow('Eroded Image', eroded)TEW

# 5. Resizing and Cropping

resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Image', resized)

cropped = img[50:200, 200:400]
cv.imshow('Cropped Image', cropped)
# 6. Warp Perspective


# 7. Joining Images


# 8. Color Detection


# 9. Contour Detection





cv.waitKey(0)