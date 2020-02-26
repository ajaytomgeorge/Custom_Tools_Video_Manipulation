#!/usr/bin/env python
"""video creator - to create a video from images"""
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

def initializer():
    global imgstack
    imgstack=[]

def videomaker(path,pathvideowrite,slicingpoints):


    def videoprocessor(path,slicingpoints):
        cap=cv2.VideoCapture(path)
        length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        print('The length {} and fps {} of the video is obtained'.format(length,fps))
        for i in range (170):
            ret,frame=cap.read()
            size=frame.shape
            for i in slicingpoints:
                imgstack.append(frame)
            else:
                try:
                    temp=np.zeros(size)
                except Exception as e:
                    print('Exception at i and size',i,size)
                imgstack.append(temp)
                imgstack.append(frame)

        return size


    def imagestacktovideo(pathvideowrite,size):
        print(size)
        print(size[0:2])
        fourcc1=cv2.VideoWriter_fourcc(*'DIVX')
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        out=cv2.VideoWriter(os.path.join(pathvideowrite,'blackinessinsertedvideo.avi'),fourcc,1,size[0:2])


        for i in range(len(imgstack)):
            try:
                print(i)
                out.write(imgstack[i])

            except Exception as e:
                fig = plt.figure()
                fig.add_subplot(1, 3, 1)
                plt.imshow(imgstack[i-2])
                fig.add_subplot(1, 3, 2)
                plt.imshow(imgstack[i-1])
                fig.add_subplot(1, 3, 3)
                plt.imshow(imgstack[i])

                plt.show(block=True)
                print ("exception ",i)

        out.release()

    size=videoprocessor(path, slicingpoints)
    print('size is ',size)
    imagestacktovideo(pathvideowrite, size)

def main():
    path='DownloadedVideos/clips/comcastclip4.mp4   '
    pathvideowrite='DownloadedVideos/finaledits'
    startframe=120
    endframe = 135
    slicingpoints=list(range(startframe,endframe))
    initializer()
    videomaker(path,pathvideowrite,slicingpoints)

if __name__=='__main__':
    main()