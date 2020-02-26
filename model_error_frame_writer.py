import cv2
import os
import numpy as np
import tensorflow as tf
from PIL import Image
from keras_preprocessing import image

directory = 'data\My Data\errorframes_macro'
filename="macrotemp"
cap = cv2.VideoCapture('comcastclip4.mp4')
i=0
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
print("length and fps is",length,fps)

#prev=frame
model = tf.keras.models.load_model('macro4.h5')
corruptno=0
previoustime=0


while(i!=length):
    ret, frame = cap.read()
    try:


        #print ("frames is",i)

        #im = Image.fromarray(frame, 'RGB')
        #im = im.resize((150,150))
        #im.save(os.path.join(directory, filename+".jpg"), "JPEG")
        cv2.imwrite(os.path.join(directory, filename+".jpg"), frame)
         #print('image path is ',os.path.join(cwd,imagepath))
        img = image.load_img(os.path.join(directory, filename+".jpg"), target_size=(150, 150))
        x = image.img_to_array(img)
        #print('x before expand _dim', x)
        x = np.expand_dims(x, axis=0)
        #print('x after expand _dim', x)
        images = np.vstack([x])
         #print('images after vstack', images)
        classes = model.predict(images, batch_size=10)
        #print(imagepath)
        print(classes)
        for classed in classes:
            #print ('classed[1] ', classed[1])
            if(classed [1]>0.):
                btime=i/fps
                if(previoustime!=int(btime)):
                    print('found blocking at time',btime)
                #im = Image.fromarray(frame, 'RGB')
                cv2.imwrite(os.path.join(directory, 'corruptedframe'+str(corruptno)+".jpg"), frame)
                #im.save(os.path.join(directory, 'corruptedframe'+str(corruptno)+".jpg"), "JPEG")
                corruptno+=1
          
        
        
    except Exception as e:
                print ('exception e',e)
    i=i+1
   

