# -*- coding: utf-8 -*-
"""
Created on Wed Oct 28 13:53:39 2020

@author: 皮皮卡卡
"""
import cv2
import numpy as np


fgbg = cv2.createBackgroundSubtractorMOG2(history=600,
                                          varThreshold=16,
                                          detectShadows=False)

TrDict = {'csrt':cv2.TrackerCSRT_create,
          'kcf': cv2.TrackerKCF_create,
          'boosting':cv2.TrackerBoosting_create,
          'mil': cv2.TrackerMIL_create,
          'tld': cv2.TrackerTLD_create,
          'medianflow': cv2.TrackerMOSSE_create}
trackers = cv2.MultiTracker_create()
#tracker = cv2.TrackerCSRT_create()

v = cv2.VideoCapture('12mm_1.mp4')
ret, frame = v.read()

for i in range(2):
    cv2.imshow('frame', frame)
    bbi = cv2.selectROI('frame', frame)
    tracker_i = TrDict['csrt']()
    trackers.add(tracker_i, frame, bbi)
    
    



width = v.get(3)
height = v.get(4)
fps = v.get(5)
frames_number = v.get(7)




         
while (v.isOpened()):
    ret ,frame = v.read()
    if ret:

        (success, boxes) = trackers.update(frame)
        
        for box in boxes:
            
            (x,y,w,h) = [int(a) for a in box]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,0),2)
            cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):                
            break
    else:
        break

v.release()
cv2.destroyAllWindows()
#data.close()
print( 'width:', width, '\n'+ 
      'height:', height, '\n'+ 
      'fps:', fps,'\n'+ 
      'frames:', frames_number)
