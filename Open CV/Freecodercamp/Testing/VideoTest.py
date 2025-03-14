import cv2

# Webcam ka resolution set karo
wCam, hCam = 1920, 1080  # Ya phir 2560, 1440 (agar webcam support kare)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, wCam)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, hCam)

if not cap.isOpened():
    print("Error: Could not access the webcam.")
else:
    cv2.namedWindow("Webcam Feed", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Webcam Feed", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imshow('Webcam Feed', frame)
        if cv2.waitKey(1) & 0xFF == ord('d'):  # 'd' dabane par exit ho jayega
            break

    cap.release()
    cv2.destroyAllWindows()
