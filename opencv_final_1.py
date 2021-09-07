# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:33:20 2020

@author: 皮皮卡卡
"""
import cv2


TrDict = {'csrt':cv2.TrackerCSRT_create,
          'kcf': cv2.TrackerKCF_create,
          'boosting':cv2.TrackerBoosting_create,
          'mil': cv2.TrackerMIL_create,
          'tld': cv2.TrackerTLD_create,
          'medianflow': cv2.TrackerMOSSE_create}

# initialize OpenCV's special multi-object tracker
tracker = TrDict['csrt']()
cap = cv2.VideoCapture('near and away10_T_T.mp4') #影片

width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)
frames_number = cap.get(7)

ret, frame = cap.read()
cv2.namedWindow("frame",0)
imS=cv2.resize(frame, (650,700))
cv2.imshow('frame', frame)
box = cv2.selectROI('frame', frame)
tracker.init(frame, box)

data = open('nearaway_l', mode='w') #黨案

while cap.isOpened():

    ret, frame = cap.read()

    if frame is None:
        break
    if box is None:
        break
    #frame = imutils.resize(frame, width=600)
    (success, box) = tracker.update(frame)

    # loop over the bounding boxes and draw them on the frame

    (x, y, w, h) = [int(a) for a in box]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # write the data in txt
    print(x+w/2,'\t',y+h/2, file=data)
    cv2.namedWindow("frame",0)
    imS=cv2.resize(frame, (650,700))

    cv2.imshow("Frame", imS)
    key = cv2.waitKey(200) & 0xFF #幾針1000/33

    # if the 's' key is selected, we are going to "select" a bounding
    # box to track

    # if you want to reset bounding box, select the 'r' key 
    if key == ord("r") or (x==0 and y==0):
        cv2.namedWindow("frame",0)
        imS=cv2.resize(frame, (650,700))
        box = cv2.selectROI("Frame", imS)
        tracker = tracker = TrDict['csrt']()

        tracker.init(frame, box)

    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
data.close()
print( 'width:', width, '\n'+ 
      'height:', height, '\n'+ 
      'fps:', fps,'\n'+ 
      'frames:', frames_number)

