import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/Cats.jpeg')


# Compute histograms for each channel (B, G, R)
colors = ('b', 'g', 'r')
for i, color in enumerate(colors):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

plt.title("RGB Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()
