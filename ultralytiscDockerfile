# #FROM osrf/ros:foxy-desktop
# FROM python:3

# Use the official YOLOv5 image as a base
FROM ultralytics/yolov5:latest

# Set the working directory
WORKDIR /usr/src/app

# Install necessary packages for accessing the webcam
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libsm-dev \
    libxkbcommon-x11-0 \
    qt5-default \
    build-essential \
    libopencv-dev

RUN pip install --upgrade pip

# Clone the YOLOv5 repository
RUN git clone https://github.com/ultralytics/yolov5.git

# Set the working directory to the YOLOv5 folder
WORKDIR /usr/src/app/yolov5

# Ensure all dependencies are installed
RUN pip install -r requirements.txt

# Default command
# CMD ["python3", "detect.py", "--source", "0", "--weights", "yolov5s.pt", "--conf", "0.25"]
CMD [ "/bin/bash" ]