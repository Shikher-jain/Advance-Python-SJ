import cv2 as cv
import numpy as np

# Create a blank image
blank = np.zeros((500, 500, 3), dtype= 'uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain color
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=2)
cv.imshow('Line', blank)

# 2. Draw a circle
cv.circle(blank,(blank.shape[1]//2, blank.shape[0]//2),44, (255,0,0), thickness=2)
cv.imshow('Circle', blank)

# 3. Draw a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2)
cv.imshow('Rectangle', blank)

# 4. Write text on an image
cv.putText(blank, 'Hello', (300,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2)   
cv.imshow('Text', blank)    

# 5. Draw a triangle
cv.line(blank,(0,0),(blank.shape[1]//2, blank.shape[0]//2), (255,0,0), thickness=2)
cv.line(blank,(blank.shape[1]//2, blank.shape[0]//2),(blank.shape[1],0), (0,0,255), thickness=2)  
cv.line(blank,(0,0),(blank.shape[1],0), (0,255,0), thickness=2)
cv.imshow('Triangle', blank)

# Wait for a key press
cv.waitKey(0)