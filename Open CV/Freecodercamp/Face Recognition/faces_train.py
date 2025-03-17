# #pylint:disable=no-member

import os
import cv2 as cv
import numpy as np

# Path to the dataset
DIR = r"C:/Users/user/Downloads/Photos CV"

# Dynamically get names from the dataset folder
people = [person for person in os.listdir(DIR) if os.path.isdir(os.path.join(DIR, person))]

haar_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
features = []
labels = []


def create_train():
    for person in people:
        print(f"Processing images for: {person}")
        path = os.path.join(DIR, person)
        label = people.index(person)
    
        for img in os.listdir(path):
            img_path = os.path.join(path, img)
            print(f"Processing image: {img_path}")
    
            img_array = cv.imread(img_path)
            if img_array is None:
                print(f"Skipping {img_path} (Unreadable or missing)")
                continue
    
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5)
    
            if len(faces_rect) == 0:
                print(f"No face detected in {img_path}")
    
            for (x, y, w, h) in faces_rect:
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()   
print(f'Training done for {len(people)} people.')

# Convert lists to NumPy arrays
features = np.array(features, dtype='object')
labels = np.array(labels)

# Train the LBPH recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

# Save the trained model
face_recognizer.save('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Face Recognition/face_trained.yml')
np.save('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Face Recognition/features.npy', features)
np.save('F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Freecodercamp/Face Recognition/labels.npy', labels)

# print(features, labels)
print(f'No. of features: {len(features)} and No. of  labels: {len(labels)}')

