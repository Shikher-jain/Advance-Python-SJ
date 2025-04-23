import cv2
import mediapipe as mp
import time

path=r"F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Advance\Face\Videos\1.mp4"
cap = cv2.VideoCapture(path)

cap.set(3, 640) 
cap.set(4, 480) 

pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=10)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:

        for faceLms in results.multi_face_landmarks:
            # mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS,drawSpec,drawSpec)
            # mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACE_CONNECTIONS)
            mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSELATION,drawSpec,drawSpec)
            # mpDraw.draw_landmarks(img, faceLms, mpFaceMesh.FACEMESH_TESSEL/ATION)

        for id,lm in enumerate(faceLms.landmark):
            #print(lm)
            ih, iw, ic = img.shape
            x,y = int(lm.x*iw), int(lm.y*ih)
            # print(id,x,y)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70), cv2.FONT_HERSHEY_PLAIN,3, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) and 0xFF == ord('q'):
        break