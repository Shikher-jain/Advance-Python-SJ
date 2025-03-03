import cv2
import matplotlib.pyplot as plt

img = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/gatewayOfIndia.jpg")
img = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/FLO.png")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)         # Grayscale
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)           # RGB
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)           # HSV
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)           # LAB
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)       # YCrCb

plt.imshow(img)
plt.show()
plt.imshow(rgb)
plt.show()
plt.imshow(hsv)
plt.show()
plt.imshow(lab)
plt.show()
plt.imshow(gray, cmap='gray')
plt.show()
plt.imshow(gray)
plt.show()
plt.imshow(ycrcb)
plt.show()


cv2.imshow("BGR", img)
cv2.imshow("RGB", rgb)
cv2.imshow("HSV", hsv)
cv2.imshow("LAB", lab)
cv2.imshow("GRAY", gray)
cv2.imshow("YCrCb", ycrcb)

cv2.waitKey(0)
cv2.destroyAllWindows()
