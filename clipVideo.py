#!/usr/bin/env python
"""clipVideo.py: Temporary Tool to clip videos using ffmpeg."""

import argparse
import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips

__author__ = "Ajay Tom George"
__credits__ = "None"
__license__ = "None"
__version__ = "1.0.1"
__maintainer__ = "Ajay Tom George"
__email__ = "ajaytomgeorge@protonmail.com"
__status__ = "R & D"

parser = argparse.ArgumentParser()

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg

def initializer():
        parser.add_argument("--j", dest="jobname",  required=True,default='clip', help="put job name merge or clip, default clip", type=str)
        parser.add_argument("--i", dest="targetname",
                            help="input the video path",nargs='+', metavar="FILE",
                            type=lambda x: is_valid_file(parser, x))

        parser.add_argument("--s",dest="start",default=10,help="start time in seconds and integers",type=int)
        parser.add_argument("--e",dest="end",default=20, help="end time in seconds and integers",type=int)

        parser.add_argument("--o", dest="destname", default='./clippedfile',required=True,
                            help="give output filepath", metavar="FILE",
                            type=str)
        #parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
        args = parser.parse_args()

def clipper(args):
    """amin funcitonality of the program is defined in this line"""
    ffmpeg_extract_subclip(args.targetname[0], args.start, args.end, targetname=args.destname)

def merger(args):
    '''
    clip = VideoFileClip("myvideo.mp4")
    clip2 = VideoFileClip("blackvideo10sec.mp4").subclip(50, 60)
    clip3 = VideoFileClip("myvideo3.mp4")
    '''
    final_clip = concatenate_videoclips(args.targetname)
    final_clip.write_videofile("my_concatenation.mp4")

def main():
    initializer()
    args = parser.parse_args()
    if args.jobname=='merge':
        merger(args)
    else:
        clipper(args)



