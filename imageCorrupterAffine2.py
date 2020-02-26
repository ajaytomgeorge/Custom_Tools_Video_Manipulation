import cv2
import random 
import numpy as np
import os
import logging
from progress.bar import Bar 
from datetime import datetime

def reportInitializer(imagename):
    currenttime=datetime.now()
    currentpath=os.getcwd()
    global dt_string
    global count
    global directory
    count=0
    dt_string = currenttime.strftime("%d_%m_%Y_%H_%M_%S")
    directory= 'ImagesGenerated/RunReportImages'+imagename+dt_string
    os.makedirs(directory)
    logging.basicConfig(filename=os.path.join(directory,'myapp.log'), level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
    global logger
    logger=logging.getLogger(__name__)

def blurrer(image_b,typecode):
    if typecode==0:
        blurImg = cv2.bilateralFilter(image_b,9,75,75) 
    elif typecode==1:
        blurImg = cv2.GaussianBlur(image_b, (5,5),0)  
    elif typecode==2:
        blurImg = cv2.medianBlur(image_b,5)  
    elif typecode<5:
        blurImg = cv2.blur(image_b,(10,10))
    else:
        blurImg = image_b
    return blurImg


def subimage(image,id, center, theta):
   ''' 
   Rotates OpenCV image around center with angle theta (in deg)
   then crops the image according to width and height.
   '''
   originalimage=image
   pureimage=image
   # Uncomment for theta in radians
   #theta *= 180/np.pi
   
   flag=0
   j=0
  
   for j in range(random.randint(5,50)):
        flag=0
        for i in range(random.randint(5,50)):
                #originalimage=pureimage
                shape = ( image.shape[1], image.shape[0] ) # cv2.warpAffine expects shape in (length, height)
                matrix = cv2.getRotationMatrix2D( center=center, angle=theta, scale=1 )
                '''warpaffine just rotates the image'''
                image = cv2.warpAffine( src=pureimage, M=matrix, dsize=shape )
                #cv2.imshow("frame",image)
                #cv2.waitKey(0)
                '''cropping defined part based on array slices'''    
                try:
                    width=random.randint(5,originalimage.shape[1]/4)
                    height=random.randint(5,originalimage.shape[0]/4)
                    x = random.randint(4,originalimage.shape[1]-width)
                    y = random.randint(4,originalimage.shape[0]-height)
                    image_cropped = image[ y:height,x:width ]
                    #cv2.imshow("frame",image_cropped)
                    #cv2.waitKey(2000)
                    x_offset=random.randint(4,originalimage.shape[1]-image_cropped.shape[1])
                    y_offset=random.randint(4,originalimage.shape[0]-image_cropped.shape[0])
                    originalimage[y_offset:y_offset+image_cropped.shape[0], x_offset:x_offset+image_cropped.shape[1]] = image_cropped
                    #cv2.imwrite(os.path.join(directory, 'blocked'+str(count)+".jpg"), originalimage)
                    #count+=1
               
                except Exception as e:
                    #logging.info('Exception Details', 'division', exc_info=e)
                    if(flag==0):
                        cv2.imwrite(os.path.join(directory, 'blocked'+str(id)+".jpg"), originalimage)
                        #count+=1
                    else:
                        flag=1
                    #count+=1
   if(flag==0):
    cv2.imwrite(os.path.join(directory, 'blocked_final'+str(id)+'.jpg'), originalimage)
   return originalimage

def main():
        mypath='./paper'
        imagename='firstrun'
        reportInitializer(imagename)
        onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]
        bar = Bar('Inserting Blockiness', max=len(onlyfiles))
        id=0   
        for v in onlyfiles:
            image = cv2.imread(os.path.join(mypath,v))
            image = subimage(image,id, center=(110, 125), theta=90)
            bar.next()
            id+=1
            #image = subimage(image, center=(random.randint(100,120), random.randint(100,130)), theta=5)
            #image = subimage(image, center=(110, 125), theta=30, width=100, height=200)
    
main()