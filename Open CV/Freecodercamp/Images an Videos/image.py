import cv2

# Read the image
img = cv2.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/FLO.png", 1)
if img is None:
    print("Error: Image not found or path is incorrect!")
else:
    print(img) 
    cv2.imshow("IMAGE", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
