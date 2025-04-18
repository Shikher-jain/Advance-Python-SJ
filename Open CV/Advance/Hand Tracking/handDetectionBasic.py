import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mpDraw = mp.solutions.drawing_utils 

pTime = 0
cTime = 0

while True:
    success , img = cap.read()
    img = cv2.flip(img, 1) 
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):

                print(f"ID: {id}, X: {lm.x}, Y: {lm.y}")            
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                print(f"ID: {id}, X: {cx}, Y: {cy}")

                cv2.circle(img, (cx, cy), 5, (255, 0, 255), cv2.FILLED)
                # cv2.circle(img, (cx, cy), 5, (255, 0, 255), -1)


            mpDraw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)
        
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
    cv2.imshow("Image", img)
    
    if cv2.waitKey(33) & 0xFF == ord('q'):
        break