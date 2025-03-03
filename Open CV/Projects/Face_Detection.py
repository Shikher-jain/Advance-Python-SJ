import cv2 as cv

# Load the pre-trained face detection model
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')


cap = cv.VideoCapture(0)

while True:
    
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv.putText(frame, 'Face', (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv.circle(frame, (x + w//2, y + h//2), w//2, (0, 0, 255), 3)
        cv.circle(frame, (x + w//3, y + h//3), 3, (0, 0, 255), 3)
        cv.circle(frame, (x + 2*w//3, y + h//3), 3, (0, 0, 255), 3)
        cv.rectangle(frame, (x + w//3, y + 2*h//3), (x + 2*w//3, y + h), (0, 255, 0), 3)

    cv.imshow('Face Detection', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv.destroyAllWindows()
