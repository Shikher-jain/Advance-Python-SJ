import cv2
import poseEstimationModule as pm
import time


path = "F:/SHIKHER-VS/Regular/Advance-Python-SJ/Open CV/Advance/Projects/AI Trainer/Videos/01.mp4"
cap = cv2.VideoCapture(path)



while True:
    success, img = cap.read()
    if not success:
        break

    detector = pm.poseDetector()
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)

    if len(lmList) != 0:
        print(lmList[0]) #0 to 32 
        cv2.circle(img, (lmList[0][1], lmList[0][2]), 10, (255,0 , 255), -1)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break