## Problem
```
>>> import cv2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/lib/python3.8/dist-packages/cv2/__init__.py", line 181, in <module>
    bootstrap()
  File "/usr/local/lib/python3.8/dist-packages/cv2/__init__.py", line 153, in bootstrap
    native_module = importlib.import_module("cv2")
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
ImportError: libGL.so.1: cannot open shared object file: No such file or directory
```
## Solution
install `libgl1-mesa-glx`

<------------------------------------------------------------------------------>

## Problem
```
Failed to save 'objectDetectionNode.py': Insufficient permissions. Select 'Retry as Sudo' to retry as superuser.
```
## Solution
Outside of docker container, run `$ sudo chown -R $USER <THE_DIRECTORY>

<------------------------------------------------------------------------------>

## Webcam not detected in VM
**Problem**: As mentioned above

**Potential Solution**: Restart the VM and ensure the camera is connected to the 
VM, not the host 