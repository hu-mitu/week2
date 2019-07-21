#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opencv-python


# In[1]:


get_ipython().system('pip install scikit-image==0.12.3')

import numpy as np
from numpy.random import rand
from numpy import uint8, float32, float64, log, pi, sin, cos, abs, sqrt

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.gray();
from matplotlib.pyplot import imshow

from skimage.io import imread, imsave
from skimage.color import rgb2gray, rgb2hsv
from skimage.transform import rotate, resize

import skimage
skmajor, skminor, sknumber = skimage.__version__.split(".")
if int(skminor) >= 11:
    from skimage.filters import threshold_otsu # version 0.11 and after
else:
    from skimage.filter import threshold_otsu # version 0.10 and before
    

from scipy.ndimage.filters import convolve

from os.path import getsize

from time import time


# In[2]:


import cv2
import os

def save_frame_camera_key(device_num, dir_path, basename, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        key = cv2.waitKey(delay) & 0xFF
        if key == ord('c'):
            cv2.imwrite('{}_{}.{}'.format(base_path, n, ext), frame)
            n += 1
        elif key == ord('q'):
            break

    cv2.destroyWindow(window_name)


save_frame_camera_key(0, 'data/temp', 'camera_capture')


# In[10]:


import cv2
import os
import datetime

def save_frame_camera_cycle(device_num, dir_path, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    n = 0
    while True:
        ret, frame = cap.read()
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            cv2.imwrite('{}_{}.{}'.format(base_path, datetime.datetime.now().strftime('%Y%m%d%H%M%S%f'), ext), frame)
        n += 1

    cv2.destroyWindow(window_name)


save_frame_camera_cycle(1, 'data/temp', 'camera_capture_cycle', 150)


# In[14]:


import cv2
import os
import datetime
import numpy as np
import matplotlib.pyplot as plt

def calc_brightness_camera(device_num, basename, cycle, ext='jpg', delay=1, window_name='frame'):
    cap = cv2.VideoCapture(device_num)
    
    if not cap.isOpened():
        return
    
    n = 0
    l = 0
    y = list()
    a = 0
    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, (int(frame.shape[1]/2), int(frame.shape[0]/2)))
        cv2.imshow(window_name, frame)
        if cv2.waitKey(delay) & 0xFF == ord('q'):
            break
        if n == cycle:
            n = 0
            l += 1
            a = frame.mean()
            y.append(a)
            x = np.arange(0, l, 1)
            
        n += 1

    
    cv2.destroyWindow(window_name)
    plt.plot(x,y)
    plt.show()
    
calc_brightness_camera(1, 'camera_capture_cycle', 1)


# In[7]:


print(x)


# In[ ]:




