# YOLOv8 Shapes Detection Model

## Overview

This repository contains the code and documentation for a shape detection model using YOLOv8. This model is designed to detect various shapes and colors in images, with a focus on scenarios where objects are far away and hard to identify.
Trying to get a best mimick for that task in our following competition.

# Sample Inference
After training and testing the model
![Finnallyyyyyyy](https://github.com/AhmedHany761/YOLOv8-/assets/134512069/201e9828-a105-43e5-bf79-4fc1a2a6dc87)
![Circle](https://github.com/AhmedHany761/YOLOv8-/assets/134512069/cbca0efb-e600-4380-b69b-b54536cb6379)

## Features

- Utilizes YOLOv8, the latest version as of January 2023, known for its accuracy and speed with compared to the four architectures evaluated  as illustrated in the following figure.
- ![1_6Sn93qyovio0qn3Y3q7Vgw](https://github.com/AhmedHany761/YOLOv8-/assets/134512069/666c1b55-373a-4119-8815-5748c9d380ba)
- Incorporates color detection in addition to shape detection.
- Simulated scenarios for objects at a distance to enhance the dataset's realism and make it more close to our desired task.
- Evaluation metrics including mean average precision (mAP) and accuracy with a good cinfusion matrix graph.
- Sample inference results showcasing model performance in two different ways
    1- Image Path: that u can import the image path u need to be detected
    2- A Connected Camera: that u can make a real time shapes detection with good performance   

## Dataset

The dataset consists of 414 images for training, and 124 and 60 images for validation and testing, respectively.
Data annotation tools and platforms were explored to improve dataset quality, although initially not required due to time constraints.
So I just start the model with Roboflow already annotated dataset.However, I explored various online platforms and tools for data annotation, which is a fascinating and an interesting experience.

## Model Training

- Hyperparameters like learning rate, batch size, and training epochs were tuned for optimal results according to many trials to get the most accurate results.
- All training data was resized to 800x800 pixels before training, affecting accuracy and speed with 25 epochs.

## Inference

Inference can be performed in two ways:
1. Using the Command Line Interface (CLI) for direct access to the pretrained YOLOv8 model.
2. Utilizing the Software Development Kit (SDK) for inference.
U should import the model and choose which way you want to detect with as a realtime detection by ur camera or through an image each task with specfic python file

## Results and Discussion

The model's performance was evaluated using metrics such as mean average precision (mAP) and accuracy with a confusion matrix graph. 
![Results Graphs](https://github.com/AhmedHany761/YOLOv8-/assets/134512069/4b04341c-ba59-4482-8f80-1b875f32ab37)
![Confusion Matrix](https://github.com/AhmedHany761/YOLOv8-/assets/134512069/26775046-1ced-4c5c-8cef-43be2f50f0be)


## Conclusion

This project aimed to develop a shape detection model using YOLOv8, with a unique dataset with images from a distance and with differnt color for detection. The combination of the latest YOLO architecture and a well-structured dataset enables accurate and efficient shape and color detection model.

## Getting Started

To get started with this project, follow the instructions in the [Installation](#installation) section below.
Also At first consider using GPU acceleration as YOLO models can be so intensive.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/yolov8-shape-detection.git
cd yolov8-shape-detection
