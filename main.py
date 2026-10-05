import cv2
from ultralytics import YOLO

def main():
    # Load the YOLOv8 model
    model = YOLO("yolov8n.pt") 

    # Initialize webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not access the webcam.")
        return

    print("Webcam started successfully. Press 'q' to exit the window.")

    # Allow the window to be resized and maximized
    cv2.namedWindow("Real-Time Object Tracking - Harsh Garg", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Dropped frame.")
            break

        # Run YOLOv8 tracking on the current frame
        # conf=0.5 ensures only confident detections are shown
        results = model.track(frame, persist=True, conf=0.5, verbose=False)

        # Generate a new frame with bounding boxes and labels drawn
        annotated_frame = results[0].plot()

        # Display the live feed
        cv2.imshow("Real-Time Object Tracking - Harsh Garg", annotated_frame)

        # Quit condition
        if cv2.waitKey(1) & 0xFF == ord("q"):
            print("Exiting...")
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()