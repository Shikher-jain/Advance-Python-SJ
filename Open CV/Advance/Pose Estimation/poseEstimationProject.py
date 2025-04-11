import cv2
import time
import poseEstimationModule as pm

# path ="F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Advance/Pose Estimation/Videos/4.mp4"
# cap = cv2.VideoCapture(path)

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()

    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        print(lmList[14]) #0 to 32 
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
    
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
