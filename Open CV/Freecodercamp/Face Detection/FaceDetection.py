import cv2  
# Load Haarcascade XML file  
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) 

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  

    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('d'): 
        break  

cap.release()
cv2.destroyAllWindows()