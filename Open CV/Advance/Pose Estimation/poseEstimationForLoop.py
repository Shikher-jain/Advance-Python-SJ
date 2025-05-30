import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()


for i in range(1, 6):
    path =f"F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Advance/Pose Estimation/Videos/{i}.mp4"
    cap = cv2.VideoCapture(path)
    pTime = 0

    while True: 
        success, img = cap.read()
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        # print(results.pose_landmarks)

        if results.pose_landmarks:
            mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                print(id, lm)
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                cv2.circle(img, (cx, cy), 5, (255, 125, 125),-1)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, f"FPS:{str(int(fps))}", (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,(255, 0, 0), 3)

        cv2.imshow(f"Image {i}", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
