import skvideo.io
import skvideo.datasets
import numpy as np

def readvideoarray():
    videodata = skvideo.io.vread(skvideo.datasets.bigbuckbunny())
    print(videodata.shape)

def writevideoarray():
    outputdata = np.random.random(size=(5, 480, 680, 3)) * 255
    outputdata = outputdata.astype(np.uint8)

    skvideo.io.vwrite("outputvideo.mp4", outputdata)

def readvideoframe():
    videogen = skvideo.io.vreader(skvideo.datasets.bigbuckbunny())
    for frame in videogen:
        print(frame.shape)

def writevideoframe():
    outputdata = np.random.random(size=(5, 480, 680, 3)) * 255
    outputdata = outputdata.astype(np.uint8)

    writer = skvideo.io.FFmpegWriter("outputvideo.mp4")
    for i in xrange(5):
        writer.writeFrame(outputdata[i, :, :, :])
    writer.close()


