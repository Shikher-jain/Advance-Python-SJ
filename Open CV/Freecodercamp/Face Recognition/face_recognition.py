# #pylint:disable=no-member

import cv2 as cv
import numpy as np
import os
   
# Load trained face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read(r'F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Freecodercamp\Face Recognition\face_trained.yml')

# Load Haar Cascade
haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load People List
DIR = r"C:/Users/user/Downloads/Photos CV"
people = [person for person in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, person))]


# -------------------------------------------------------
# video test by me
cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)
    for (x, y, w, h) in faces_rect:
        faces_roi = gray[y:y+h, x:x+w]

        label, confidence = face_recognizer.predict(faces_roi)
        print(f'Label: {people[label]} | Confidence: {confidence:.2f}')

        color = (0, 255, 0) if confidence < 50 else (0, 0, 255)  # Green for high accuracy, Red for low
        cv.rectangle(frame, (x, y), (x + w, y + h), color, thickness=2)
        cv.putText(frame, people[label], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)

    cv.imshow('Face Recognition', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()

# -------------------------------------------------------

# Load Test Image
# test_img_path = r"C:/Users/user/Downloads/Photos CV/Yogi/yogi3.jpeg"
# img = cv.imread(test_img_path)

# if img is None:
#     print("Error: Image not found!")
# else:
#     gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#     # Detect Faces
#     faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

#     for (x, y, w, h) in faces_rect:
#         faces_roi = gray[y:y+h, x:x+w]

#         label, confidence = face_recognizer.predict(faces_roi)
#         print(f'Label: {people[label]} | Confidence: {confidence:.2f}')

#         color = (0, 255, 0) if confidence < 50 else (0, 0, 255)  # Green for high accuracy, Red for low
#         cv.rectangle(img, (x, y), (x + w, y + h), color, thickness=2)
#         cv.putText(img, people[label], (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)

    ## Resize if too large

    # resized = cv.resize(img, (800, 600))
    # cv.imshow('Face Recognition', resized)

    # cv.waitKey(0)
    # cv.destroyAllWindows()
