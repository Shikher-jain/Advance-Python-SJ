import cv2

img = cv2.imread('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Cats.jpeg',0)

# Apply adaptive thresholding
adaptive_thresh_mean = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_thresh_gaussian = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

adaptive_thresh_mean_inv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 11, 2)
adaptive_thresh_gaussian_inv = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

cv2.imshow('Adaptive Mean', adaptive_thresh_mean)
cv2.imshow('Adaptive Gaussian', adaptive_thresh_gaussian)

cv2.imshow('Bitwise Adaptive Mean', cv2.bitwise_not(adaptive_thresh_mean))
cv2.imshow('Bitwise Adaptive Gaussian', cv2.bitwise_not(adaptive_thresh_gaussian))

cv2.imshow('Adaptive Mean Inv', adaptive_thresh_mean_inv)
cv2.imshow('Adaptive Gaussian Inv', adaptive_thresh_gaussian_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
