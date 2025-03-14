import cv2

cap = cv2.VideoCapture(0)  # Webcam open karega

while True:
    ret, frame = cap.read()
    cv2.imshow('Webcam', frame)

    # Agar user 'q' press kare to loop exit ho jaye
    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
