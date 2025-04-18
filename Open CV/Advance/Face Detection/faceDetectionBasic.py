import cv2
import mediapipe as mp  
import time

pTime = 0
cap =cv2.VideoCapture(0)

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.75)

# mpDrawStyles = mp.solutions.drawing_styles          

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Flip the image horizontally
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = faceDetection.process(imgRGB)

    # print(results.detections)

    if results.detections:
        for id, detection in enumerate(results.detections):
            mpDraw.draw_detection(img, detection)

            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)

            bBoxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape

            bbox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih), \
                   int(bBoxC.width * iw), int(bBoxC.height * ih)
            
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f"{str(int(detection.score[0]*100)) }%", (bbox[0],bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 2,(255,0,255),2)

                
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS:{str(int(fps))}", (30, 50), cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

