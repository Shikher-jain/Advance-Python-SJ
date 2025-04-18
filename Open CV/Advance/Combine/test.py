# hand tracking, face detection, and pose estimation 

import cv2
import time
import mediapipe as mp

import handTrackingModule as htm
import faceDetectionModule as fdm
import poseEstimationModule as pm

# Initialize video capture (0 for webcam or give video file path)
# cap = cv2.VideoCapture("F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Advance/Pose Estimation/Videos/5.mp4")
cap = cv2.VideoCapture(0)

# Initialize detectors
handDetector = htm.handDetector()
faceDetector = fdm.FaceDetector()
poseDetector = pm.poseDetector()

pTime = 0  # Previous time for FPS calculation

while True:
    success, img = cap.read()
    if not success:
        print("Failed to grab frame.")
        break

    # Hand Tracking
    img = cv2.resize(img, (640, 480))  # Resize to 640x480 or even 320x240

    img = cv2.flip(img, 1)  # Flip the image horizontally
    img = handDetector.findHands(img)
    lmList = handDetector.findPositins(img)
    if len(lmList) != 0:
        print("Hand Landmark 4:", lmList[4])  # Tip of thumb

    # Face Detection
    img, bboxes = faceDetector.findFaces(img, draw=True)
    if len(bboxes) != 0:
        print("Face BBox:", bboxes[0])  # First detected face

    # Pose Estimation
    img = poseDetector.findPose(img)
    poseLms = poseDetector.findPosition(img, draw=False)
    if len(poseLms) != 0:
        print("Pose Landmark 14:", poseLms[14])  # E.g., right elbow
        cv2.circle(img, (poseLms[14][1], poseLms[14][2]), 15, (0, 0, 255), cv2.FILLED)

    # Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime

    # Display FPS
    cv2.putText(img, f'FPS: {int(fps)}', (10, 70),
                cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Show Image
    cv2.imshow("Merged Detection", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
