import cv2 as cv
img=cv.imread("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Photos/gatewayOfIndia.jpg")
for i in range(0,10):
    cv.imshow(f'Gateway of India {i} ',img)
    if cv.waitKey(1) & 0xFF=="d":
        break
cv.waitKey(0)

