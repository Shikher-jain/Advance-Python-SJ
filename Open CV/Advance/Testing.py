import cv2
import time

cap = cv2.VideoCapture(0)
pTime = 0

while True:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    print(fps)
    cv2.imshow("Test FPS", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


