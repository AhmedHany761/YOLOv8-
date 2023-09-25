from ultralytics import YOLO
import cv2

# Initialize the YOLO model
model = YOLO('best.pt')

# Open a connection to the laptop's camera (usually camera index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Perform object detection on the captured frame
    results = model(source=frame, show=True, conf=0.4)
    
    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
 