import cv2
import time
import os


print(os.path.dirname(os.path.abspath(__file__)))  #+"\\Face\\Videos\\1.mp4"
path = os.path.dirname(os.path.abspath(__file__)) + "\\Face\\Videos\\1.mp4"
# path = r'F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Advance\Face\Videos\1.mp4'

cap = cv2.VideoCapture(path)
cap.set(3, 320) 
cap.set(4, 240) 

pTime = 0

while True:
# while 0:
    success, img = cap.read()
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    print(fps)
    cv2.imshow("Test FPS", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


