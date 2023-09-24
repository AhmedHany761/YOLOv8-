from ultralytics import YOLO
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Initialize the YOLO model
model = YOLO('best.pt')

# Specify the path to the image you want to process
image_path = r"C:\Users\Lenovo\Downloads\Yaarbbb.jpg"

# Perform object detection on the image
results = model(source=image_path, show=True, conf=0.4, save=True)

# Display the image with bounding boxes around detected objects
image = mpimg.imread("runs/detect/predict/Yaarbbb.jpg")
plt.figure(figsize=(10, 10))
plt.imshow(image)
plt.axis('off')  # Hide axes
plt.show()
