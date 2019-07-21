#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install opencv-python


# In[6]:


get_ipython().system('pip install scikit-image==0.12.3')


# In[8]:


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

