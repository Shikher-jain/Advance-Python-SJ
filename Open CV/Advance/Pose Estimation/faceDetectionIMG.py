import cv2
import mediapipe as mp
import time

# Load image
img = cv2.imread(r"F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Advance\Face Detection\gp.jpeg")
img = cv2.resize(img, (640, 480))  # Resize for better performance

pTime = 0
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(0.5)  # Reduced threshold

imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = faceDetection.process(imgRGB)

if results.detections:
    for id, detection in enumerate(results.detections):
        bBoxC = detection.location_data.relative_bounding_box
        ih, iw, ic = img.shape

        bbox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih), \
               int(bBoxC.width * iw), int(bBoxC.height * ih)

        cv2.rectangle(img, bbox, (255, 0, 255), 2)
        cv2.putText(img, f"{int(detection.score[0] * 100)}%", 
                    (bbox[0], bbox[1] - 10), 
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

cTime = time.time()
fps = 1 / (cTime - pTime)
pTime = cTime

cv2.putText(img, f"FPS:{int(fps)}", (30, 50),
            cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

cv2.imshow("Detected Faces", img)

cv2.waitKey(0)
cv2.destroyAllWindows()