#!/usr/bin/env python
"""download_videos_youtube.py: download videos from youtube and other tube sites.
Feed the urls in excel sheet Youtube-urls-data.xlsx, files will be downloaded to DownloadedVideos """


import pafy
import pandas as pd
import os
import argparse

__author__ = "Ajay Tom George"
__credits__ = "None"
__license__ = "None"
__version__ = "1.0.1"
__maintainer__ = "Ajay Tom George"
__email__ = "ajaytomgeorge@protonmail.com"
__status__ = "R & D"

def initializer():
    parser=argparse.ArgumentParser()
    parser.add_argument("--j",dest="jobname",required=True,help='give desc(single word) of type of videos')
    args=parser.parse_args()

    if not os.path.exists(os.path.join('./DownloadedVideos',args.jobname)):
        os.makedirs(os.path.join('./DownloadedVideos',args.jobname))
    return args.jobname

def main(jobname):
    df = pd.read_excel('Youtube-urls-data.xlsx', sheetname='urldata')
    for i in df.index:
        print(df['Youtube_Urls'][i])
        primaryurl = df['Youtube_Urls'][i];
        video = pafy.new(primaryurl)

        streams = video.streams
        for i in streams:
            print(i)

            # best = video.getbest()
        best = video.getbest(preftype="mp4")
        print(jobname)
        best.download(filepath='./DownloadedVideos/'+jobname)

if __name__=="__main__":
    main(initializer())
