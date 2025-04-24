import cv2
import os

# 🧑‍💻 Step 1: Enter your name
name = input("Enter your name: ").strip()

# 📁 Step 2: Create folder path
dataset_path = r"F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Advance\Face Capture\dataset"
folder_path = os.path.join(dataset_path, name)
os.makedirs(folder_path, exist_ok=True)

# 📷 Step 3: Start webcam
cap = cv2.VideoCapture(0)
count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Capturing Faces - Press 'c' to capture, 'q' to quit", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):
        img_path = os.path.join(folder_path, f"{count}.jpg")
        cv2.imwrite(img_path, frame)
        count += 1
        print(f"[INFO] Captured {count} image(s)")

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
