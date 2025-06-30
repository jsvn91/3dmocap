from cvzone.PoseModule import PoseDetector
import cv2
# x1,y1,z1,x2,y2,z2
cap = cv2.VideoCapture("./videos/exported_video.mp4")

detector = PoseDetector()
posList = []
final = {
    x:[] for x in range(0,33)
}

while True:
    success,img = cap.read()
    try:
        img = detector.findPose(img)
    except:
        break

    lmList,bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ""
        for no,lm in enumerate(lmList):
            # print(lm)
            lmString += f"{lm[1]},{img.shape[0]-lm[2]},{abs(lm[3])},"
            final[no].append(lmList)

        posList.append(lmString)

    # print(posList)
    # cv2.imshow("Image",img)
    key = cv2.waitKey(1)

import json

with open('data.json', 'w') as f:
    json.dump(final, f)

with open('data.json', 'r') as handle:
    parsed = json.load(handle)

f = open("parsed.json",'w')
print(json.dumps(parsed, indent=4),file=f)