import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import sys

class VolumeGestureApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gesture Volume Control 🎛️")
        self.root.geometry("400x300")
        self.source = tk.IntVar(value=0)
        self.video_path = ""

        tk.Label(root, text="Select Video Source 🎥", font=("Helvetica", 16)).pack(pady=20)

        tk.Radiobutton(root, text="Default Webcam (0)", variable=self.source, value=0).pack(anchor='w', padx=40)
        tk.Radiobutton(root, text="External Camera (1)", variable=self.source, value=1).pack(anchor='w', padx=40)
        tk.Radiobutton(root, text="Video File", variable=self.source, value=2).pack(anchor='w', padx=40)

        self.browse_button = tk.Button(root, text="Browse Video File", command=self.browse_video)
        self.browse_button.pack(pady=10)

        self.start_button = tk.Button(root, text="Start Gesture Control ▶️", command=self.start_gesture_control, bg="#28a745", fg="white")
        self.start_button.pack(pady=20)

    def browse_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4 *.avi *.mov")])
        if self.video_path:
            messagebox.showinfo("Selected", f"Video selected:\n{self.video_path}")

    def start_gesture_control(self):
        source_type = self.source.get()

        if source_type == 2 and not self.video_path:
            messagebox.showerror("Error", "Please select a video file.")
            return

        # Pass video source to script
        video_arg = str(source_type) if source_type != 2 else self.video_path
        subprocess.Popen([sys.executable, "Advance-Python-SJ\\Open CV\\Advance\\Projects\\Volume\\HandvolumeGesture.py", video_arg])

# Run GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = VolumeGestureApp(root)
    root.mainloop()
# F:\SHIKHER-VS\Regular\Advance-Python-SJ\Open CV\Advance\Projects\Volume\HandVolumeGesture.py