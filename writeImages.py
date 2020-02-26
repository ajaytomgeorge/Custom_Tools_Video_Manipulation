import cv2
import os

path1 = 'data\Dataset'
cap = cv2.VideoCapture(os.path.join(path1 ,'comcasttest.mp4'))
i=0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("length and fps is",length,fps)

#prev=frame

while(i!=length):
    ret, frame = cap.read()
    try:

        #res = cv2.absdiff(prev, frame)
        #res = res.astype(np.uint8)
        #percentage = (numpy.count_nonzero(res) * 100)/ res.size
        #if(percentage>75):
            #continue


        print ("frames is",i)
        path2 = 'data\\Dataset\\pearsyImages'
        if(True):
            cv2.imwrite(os.path.join(path2 , "c10-" + str(i) + ".jpg"), frame)
        
    except Exception as e:
                print ('exception e',e)
    i=i+1
   

