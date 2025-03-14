# Face Detection: Blue Box
# Eye Detection: Green Box
# Smile Detection: Yellow Box
# Mask Detection:
# Mask hai → Green Box 😷
# Mask nahi hai → Red Box ❌

import cv2
import numpy as np
from tensorflow.keras.models import load_model

# Haarcascade classifiers load karo  
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")

# ✅ Mask detection model ko sahi format me load karo  
try:
    mask_model = load_model(r"F:\SHIKHER-VS\Advance-Python-SJ\Open CV\Projects\mask_detector.h5")
  # Ensure correct format
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Webcam open karo  
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # **Face Detection (Blue Box)**
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # **Eye Detection (Green Box)**
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

        # **Smile Detection (Yellow Box)**
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 255), 2)

        # **Mask Detection**
        roi_resized = cv2.resize(roi_color, (224, 224))
        roi_normalized = roi_resized / 255.0
        roi_reshaped = np.reshape(roi_normalized, (1, 224, 224, 3))

        prediction = mask_model.predict(roi_reshaped)
        label = "Mask Detected 😷" if prediction[0][0] > 0.5 else "No Mask Detected ❌"
        color = (0, 255, 0) if prediction[0][0] > 0.5 else (0, 0, 255)

        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)

    cv2.imshow("Advanced Face Detection System", frame)

    if cv2.waitKey(1) & 0xFF == ord("d"):
        break

cap.release()
cv2.destroyAllWindows()
