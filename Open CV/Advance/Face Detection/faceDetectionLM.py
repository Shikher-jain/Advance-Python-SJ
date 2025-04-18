import cv2
import mediapipe as mp  
import time

# Initialize webcam
cap = cv2.VideoCapture(0)
pTime = 0

# MediaPipe setup
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection(model_selection=0, min_detection_confidence=0.75)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  # Flip horizontally for mirror effect
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    results = faceDetection.process(imgRGB)

    if results.detections:
        for id, detection in enumerate(results.detections):
            # Draw bounding box and confidence
            bBoxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bBoxC.xmin * iw), int(bBoxC.ymin * ih), \
                   int(bBoxC.width * iw), int(bBoxC.height * ih)
            cv2.rectangle(img, bbox, (255, 0, 255), 2)
            cv2.putText(img, f"{int(detection.score[0] * 100)}%", 
                        (bbox[0], bbox[1] - 20),
                        cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

            # Draw landmarks with IDs
            for lm_id, keypoint in enumerate(detection.location_data.relative_keypoints):
                kp_x = int(keypoint.x * iw)
                kp_y = int(keypoint.y * ih)
                cv2.circle(img, (kp_x, kp_y), 5, (0, 0, 255), cv2.FILLED)
                cv2.putText(img, str(lm_id), (kp_x + 5, kp_y - 5),
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)

    # Calculate and display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f"FPS: {int(fps)}", (30, 50), 
                cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 3)

    cv2.imshow("Face Detection with Landmark IDs", img)

    # Quit with 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
