# trilaterationBasedOdometry
A method of deriving the odometry of an object of known size via monocular camera based trilateration

## Installation
```
pip install opencv-python cvzone mediapipe
```

Getting the USB Webcam to work on WSL (within my venv) was accomplished using the sintructions found 
in the following two links: 
1. [Microsoft instructions](https://learn.microsoft.com/en-us/windows/wsl/connect-usb)
2. [Driver instructions](https://www.youtube.com/watch?v=t_YnACEPmrM&ab_channel=AgileDevArt)
    - additionally, I had to run `$ sudo apt install bc`

## Design
I completed my project in iteratively more complex modules. These modules were as follows:
1. Get face measurement detection working
2. Train a pytorch model on my drone using what I learned in 1.
3. Create a ROS2 container and run 2. from it
4. Create a package in my container that allows me to move a point around in RVIZ based on keyboard input
5. ???
6. Replace my pytorch model with a homemade tensorflow lite model


Kalman filter 
height estimate
visio nbased localization of each camera