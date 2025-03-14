import cv2

img = cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/Cats.jpeg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blurred, 50, 150)  

cv2.imshow("Canny Edge Detection", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
