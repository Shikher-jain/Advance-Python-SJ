import cv2
import numpy as np

# Load Image
image = cv2.imread(r'F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Freecodercamp\Cats.jpeg')
cv2.imshow("Original Image", image)

# Convert to HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Create a blank mask
blank = np.zeros(image.shape[:2], dtype='uint8')

# 1️⃣ Binary Masking (Circular ROI)
binary_mask = blank.copy()
cv2.circle(binary_mask, (150, 150), 100, 255, -1)
binary_result = cv2.bitwise_and(image, image, mask=binary_mask)

# 2️⃣ Bitwise Masking (Rectangle)
bitwise_mask = blank.copy()
cv2.rectangle(bitwise_mask, (50, 50), (200, 200), 255, -1)
bitwise_result = cv2.bitwise_and(image, image, mask=bitwise_mask)


# 3️⃣ Color Masking (Detecting Red Color)
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])
color_mask = cv2.inRange(hsv, lower_red, upper_red)
color_result = cv2.bitwise_and(image, image, mask=color_mask)

# 4️⃣ Edge Masking (Canny Edge Detection)
edges = cv2.Canny(image, 100, 200)
edge_result = cv2.bitwise_and(image, image, mask=edges)  # Fix here: Use edges as mask

# 5️⃣ Background Removal (GrabCut Algorithm)
grabcut_mask = np.zeros(image.shape[:2], np.uint8)
grabcut_mask2 =  blank.copy()

bgd_model = np.zeros((1, 65), np.float64)
fgd_model = np.zeros((1, 65), np.float64)
rect = (50, 50, 300, 300)  # ROI
cv2.grabCut(image, grabcut_mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
cv2.grabCut(image, grabcut_mask2, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)

# Modify the mask for proper segmentation
grabcut_mask = np.where((grabcut_mask == 2) | (grabcut_mask == 0), 0, 1).astype('uint8')
grabcut_result = image * grabcut_mask[:, :, np.newaxis]
grabcut_mask2 = np.where((grabcut_mask2 == 2) | (grabcut_mask2 == 0), 0, 1).astype('uint8')
grabcut_result2 = image * grabcut_mask2[:, :, np.newaxis]

# Display Results
cv2.imshow("Binary Masking", binary_result)
cv2.imshow("Bitwise Masking", bitwise_result)
cv2.imshow("Color Masking (Red)", color_result)
cv2.imshow("Edge Masking", edge_result)
cv2.imshow("Background Removal (GrabCut)", grabcut_result)
cv2.imshow("Background Removal (GrabCut) 2", grabcut_result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
