from cvzone.PoseModule import PoseDetector
import cv2
# x1,y1,z1,x2,y2,z2
cap = cv2.VideoCapture("./videos/exported_video.mp4")

detector = PoseDetector()
posList = []

while True:
    success,img = cap.read()
    try:
        img = detector.findPose(img)
    except:
        break

    lmList,bboxInfo = detector.findPosition(img)
    rigid = {"head_bone":[],
             "trunk":[],
             "nose":lmList[0],
             "":""
             }
    if bboxInfo:
        lmString = ""
        for lm in lmList:
            # print(lm)
            lmString += f"{lm[1]},{img.shape[0]-lm[2]},{abs(lm[3])},"

        posList.append(lmString)

    print(posList)
    cv2.imshow("Image",img)
    key = cv2.waitKey(1)
    # if key==ord('s'):

def partition(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

with open("batsman_anim.txt",'w') as f:
    # f.writelines([ f"%s\n" % item for item in posList])
    f.writelines([ f"%s\n" % list(partition(eval(item),3)) for item in posList] )


