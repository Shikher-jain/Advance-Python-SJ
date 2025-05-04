import numpy as np
import cv2

imgCanvas = np.zeros((720,1280,3), np.uint8)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Width
cap.set(4, 720)   # Height

while True:
    success, image = cap.read()
    image = cv2.flip(image, 1)  # Flip the image horizontally
    bitwiseOR = cv2.bitwise_or(image, imgCanvas, image)  # Combine the canvas with the image
    cv2.imshow("Image", image)
    cv2.imshow("Canvas", imgCanvas)
    cv2.imshow("Bitwise OR", bitwiseOR)  # Show the combined image
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break