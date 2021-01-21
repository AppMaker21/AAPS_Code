import time
import socket
import numpy as np
import cv2
from picamera import PiCamera

camera = PiCamera()
size = (1920, 1080)
camera.resolution = size

def takePic(path=None):
    if path is not None:
        start = time.time()
        camera.capture(path)
        end = time.time()
        print("Trigger time: " + str(end-start))
        data = None
    elif path is None:
        start = time.time()
        data = np.empty((size[1], size[0], 3), dtype=np.uint8)
        # np.epmpty ( (second pixel is height, first pixel is width) , unsigned int with 8 bits)
        camera.capture(data, "bgr")
        end = time.time()
        print("Trigger time: " + str(end-start))
    return data

