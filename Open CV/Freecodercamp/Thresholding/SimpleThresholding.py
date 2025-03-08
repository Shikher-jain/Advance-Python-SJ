import cv2

img = cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Cats.jpeg',0)
# Apply simple thresholding
th, binary_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_, binary_inv_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_, trunc_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_, tozero_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_, tozero_inv_thresh = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)


print(th)
# Display results
cv2.imshow('Image', img)
cv2.imshow('Binary', binary_thresh)
cv2.imshow('Binary Inverse', binary_inv_thresh)
cv2.imshow('Trunc', trunc_thresh)
cv2.imshow('To Zero', tozero_thresh)
cv2.imshow('To Zero Inverse', tozero_inv_thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
