# Real-Time Object Detection and Tracking 📷

**CodeAlpha AI Internship - Task 4**

## 📝 Project Overview
This project is my final submission for the CodeAlpha Artificial Intelligence Internship. It is a Python-based computer vision script that captures live video from a webcam and performs real-time object detection and multi-object tracking. 

Given hardware constraints (running entirely on a CPU), I specifically optimized the project to use the Ultralytics YOLOv8 Nano model, which provides a perfect balance of speed and accuracy without requiring a dedicated GPU.

## ✨ Key Features
- **Real-Time Detection:** Identifies multiple classes of objects simultaneously through the live webcam feed.
- **Persistent Tracking:** Unlike basic detection, this script assigns a unique ID to each detected object and tracks its movement across frames (using YOLO's built-in tracking capabilities).
- **CPU Optimized:** Utilizes `yolov8n.pt` (the nano variant) to ensure smooth FPS on standard laptop hardware.
- **Live Annotations:** Automatically draws bounding boxes, class labels, tracking IDs, and confidence scores directly onto the video feed using OpenCV.

## 🛠️ Tech Stack
- **Python 3:** Core programming language.
- **OpenCV (`opencv-python`):** Used for video capturing, frame manipulation, and GUI display.
- **Ultralytics (YOLOv8):** The state-of-the-art model used for inference and tracking.

## 🧠 What I Learned
Working on this computer vision task taught me a lot about processing video data:
- **Detection vs. Tracking:** I learned the technical difference between just finding an object in an isolated frame and maintaining its state/ID continuously using `persist=True`.
- **Frame Loops:** Handling a continuous `while True` loop to read frames via `cv2.VideoCapture()`, process them through the neural network, and render them back in milliseconds.
- **Resource Management:** The importance of properly releasing hardware resources (`cap.release()`) and destroying windows to prevent memory leaks after the script finishes execution.

## 🚀 How to Run Locally
1. Ensure Python 3 is installed on your system.
2. Clone this repository.
3. Install the required dependencies using pip:
   `pip install ultralytics opencv-python`
4. Run the script from your terminal:
   `python main.py`
5. Press the **'q'** key on your keyboard while the video window is active to safely exit the application.

---
*Designed and Developed by Harsh Garg*