import cv2

# 🔍 Local file path (change it to your actual video location)

input_path ="F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Advance/Pose Estimation/Videos/1.mp4"
output_path ="F:/SHIKHER-VS/Advance-Python-SJ/Open CV/Advance/Pose Estimation/Videos/6.mp4"


# ✅ Desired size
new_width = 450
new_height = 640

# 🎥 Read video
cap = cv2.VideoCapture(input_path)

# 🛠️ Setup video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter(output_path, fourcc, fps, (new_width, new_height))

# 🔁 Resize frame by frame
while True:
    ret, frame = cap.read()
    if not ret:
        break
    resized_frame = cv2.resize(frame, (new_width, new_height))
    out.write(resized_frame)

# ✅ Cleanup
cap.release()
out.release()
print("Video resized successfully and saved at:")
print(output_path)
