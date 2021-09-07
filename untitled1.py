import imutils
import cv2

trackerName = 'csrt'


OPENCV_OBJECT_TRACKERS = {
    "csrt": cv2.TrackerCSRT_create,
    "kcf": cv2.TrackerKCF_create,
    "boosting": cv2.TrackerBoosting_create,
    "mil": cv2.TrackerMIL_create,
    "tld": cv2.TrackerTLD_create,
    "medianflow": cv2.TrackerMedianFlow_create,
    "mosse": cv2.TrackerMOSSE_create
}

# initialize OpenCV's special multi-object tracker
trackers = cv2.MultiTracker_create()
cap = cv2.VideoCapture('0mm_1.mp4')
width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)
frames_number = cap.get(7)
while cap.isOpened():

    ret, frame = cap.read()

    if frame is None:
        break

    #frame = imutils.resize(frame, width=600)
    (success, boxes) = trackers.update(frame)

    # loop over the bounding boxes and draw them on the frame
    for box in boxes:
        (x, y, w, h) = [int(a) for a in box]
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(33) & 0xFF

    # if the 's' key is selected, we are going to "select" a bounding
    # box to track
    if key == ord("s"):
        colors = []
        # select the bounding box of the object we want to track (make
        # sure you press ENTER or SPACE after selecting the ROI)
        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                             showCrosshair=True)
        box = tuple(map(tuple, box)) 
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

    # if you want to reset bounding box, select the 'r' key 
    elif key == ord("r"):
        trackers.clear()
        trackers = cv2.MultiTracker_create()

        box = cv2.selectROIs("Frame", frame, fromCenter=False,
                            showCrosshair=True)
        box = tuple(map(tuple, box))
        for bb in box:
            tracker = OPENCV_OBJECT_TRACKERS[trackerName]()
            trackers.add(tracker, frame, bb)

    elif key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
print( 'width:', width, '\n'+ 
      'height:', height, '\n'+ 
      'fps:', fps,'\n'+ 
      'frames:', frames_number)