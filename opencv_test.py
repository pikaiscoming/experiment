# -*- coding: utf-8 -*-
"""
Created on Sat Oct 10 15:10:42 2020

@author: User
"""


import cv2
import numpy as np

cap = cv2.VideoCapture('6mm.mp4')







while (cap.isOpened()):
    ret, frame = cap.read()
    fps = cap.get(cv2.CAP_PROP_FPS)
    
   


    if ret:        