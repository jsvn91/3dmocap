# TechVidvan Human pose estimator
# import necessary packages

import cv2
import mediapipe as mp
from cvzone.PoseModule import PoseDetector

# create capture object
cap = cv2.VideoCapture("./videos/exported_video.mp4")

# initialize Pose estimator
mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

pose = mp_pose.Pose(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5)
detector = PoseDetector()
posList = []
final = {}
frames = []
while cap.isOpened():

    try:
        # read frame from capture object
        _, frame = cap.read()
        # frame = cv2.bitwise_not(frame)
        img = detector.findPose(frame)
        lmList, bboxInfo = detector.findPosition(img)
        if lmList:
            frames.append(lmList)

        # convert the frame to RGB format
        RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # process the RGB frame to get the result
        results = pose.process(RGB)
        print(results.pose_landmarks)

        # draw detected skeleton on the frame
        mp_drawing.draw_landmarks(
            frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # show the final output
        # cv2.imshow('Output', frame)

    except:
        break

    if cv2.waitKey(1) == ord('q'):
        break
    # cap.release()
    # cv2.destroyAllWindows()
with open("batsman_anim_2.txt",'w') as f:
    for i in frames:
        print(str([ str(f[1:]) for f in i ]).replace("[","").replace("]",""),file=f)
