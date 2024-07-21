# Use an official ROS distribution as a parent image
FROM ros:noetic

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive

RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

RUN apt update && apt install -y curl

RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -

RUN /bin/bash -c "echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc"

# Install packages to get everything running
RUN apt update && apt upgrade -y && apt-get install -y \ 
    python3-rosdep \
    python3-rosinstall-generator \
    python3-wstool \
    build-essential \
    python3-pip \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libx11-dev \
    libxext-dev \
    libxrender-dev \
    libsm-dev \
    libxkbcommon-x11-0 \
    qt5-default \
    libopencv-dev \
    && rm -rf /var/lib/apt/lists/*

# Install packages to get auxiliary packages running
RUN pip3 install --upgrade pip && \
    pip3 install opencv-python-headless \
    ultralytics    

# Update rosdep, numpy, and the system as a whole
RUN rosdep update && \
    pip3 install --upgrade numpy && \
    apt-get update

WORKDIR /root

CMD [ "/bin/bash" ]