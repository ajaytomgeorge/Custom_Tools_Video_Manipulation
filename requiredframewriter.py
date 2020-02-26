import cv2
import os
import numpy as np



videopath='mergedpriyankaad.mp4'
cap = cv2.VideoCapture(videopath)
filename = videopath.split('.')[0]
directory = os.path.join('Selectedframes',filename)
if(not os.path.exists(directory)):
    os.mkdir(directory)

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("length and fps is", length, fps)

framestocapture=list(range(420,430))
#framestocapture=[*list(range(250,325)),*list(range(430,450))]
for i in range(length):
    ret, frame = cap.read()
    try:
        if i in framestocapture:
            cv2.imwrite(os.path.join(directory, filename+str(i) + ".png"), frame)
            print('Writing frame ',i)
    except Exception as e:
        print('exception e', e)



