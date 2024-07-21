# Wednesday June 26

Commands for the Docker file and yolo model:

```
docker run --privileged \
    --env QT_X11_NO_MITSHM=1 \
    -e DISPLAY \
    -v /tmp/.X11-unix:/tmp/.X11-unix \
    -v /dev/video0:/dev/video0 \
    -v /dev/video1:/dev/video1 \
    -v /home/bradley/Desktop/Workspace/trilaterationBasedOdometry:/root \
    -it \
    --rm \
    --device /dev/video0 \
    ros-container

python3 detect.py --source 0 --weights yolov5s.pt --conf 0.25 --device cpu
```

TODO
- [ ] Get a distance yolo model working on the cpu
- [ ] Figure out how to run yolo gui applications in this container
- [ ] Build a better image (with support for ROS, YOLO, OpenCV, etc)

# Friday June 28
* I've gotten the 