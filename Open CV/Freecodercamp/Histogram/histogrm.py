import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Cats.jpeg')
cv.imshow('Cats', img)                                                                                    

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Grayscale Histogram
gray_hist = cv.calcHist([img], [0], None, [256], [0, 270])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 300])
plt.show()

cv.imshow('Gray Histo', gray_hist)
cv.waitKey(0)
cv.destroyAllWindows()