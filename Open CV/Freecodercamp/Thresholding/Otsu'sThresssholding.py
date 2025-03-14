import cv2

img = cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/Cats.jpeg',0)

# Apply Otsu's thresholding
_, otsu_thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
_, otsu_thresh_inv = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU_INV)

cv2.imshow('Otsu Thresholding', otsu_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
