import cv2
import os
import shutil
from cvzone.PoseModule import PoseDetector

#opening the video
#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture("Video2.mp4")


detector= PoseDetector()
posList= []
while True:
    success, img= cap.read()
    #ResizedImg = cv2.resize(img, (960,540), interpolation=cv2.INTER_LINEAR)
    img= detector.findPose(img)
    cv2.imshow("Image", img)
    lmList, bboxInfo= detector.findPosition(img)

    if bboxInfo:
        #creating the list with the co-ordinates
        lmString= ''
        for lm in lmList:
           #print(lm)
            lmString += f'{lm[1]},{img.shape[0] - lm[2]},{lm[1]},'
        posList.append(lmString)

    print(len(posList))

    #cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    #save button 's'
    if key == ord('s'):
        #os.remove("AnimationFile2.txt")
        with open("AnimationFile.txt", 'w') as f:
            f.writelines(["%s\n" % item for item in posList])
        src_path = r"C:\Users\Admin\PycharmProjects\MotionCapture\AnimationFile.txt"
        dst_path = r"C:\Users\Admin\PycharmProjects\MotionCaptureUnity\Assets\AnimationFile.txt"
        shutil.copy(src_path, dst_path)
        cv2.destroyAllWindows()
        break

