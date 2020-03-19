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

parser.add_argument("--j", dest="jobname", required=True, default='clip',
                    help="put job name merge or clip, default clip", type=str)
parser.add_argument("--t", dest="targetname",
                    help="input the video path", nargs='+', metavar="FILE",
                    type=str)
'''
parser.add_argument("--i", dest="targetname",
                    help="input the video path",nargs='+', metavar="FILE",
                    type=lambda x: is_valid_D:\767473_Lipsync\LipNet-master\assets\police_10.mp4file(parser, x))
'''
parser.add_argument("--s", dest="start", default=10, help="start time in seconds and integers", type=int)
parser.add_argument("--e", dest="end", default=15, help="end time in seconds and integers", type=int)

parser.add_argument("--o", dest="destname", default='clippedfile.mp4',
                    help="give output filepath", metavar="FILE",
                    type=str)
# parser.add_argument("-v", "--verbose", help="increase output verbosity",action="store_true")
args = parser.parse_args()

def is_valid_file(parser, arg):
    if not os.path.exists(arg):
        parser.error("The file %s does not exist!" % arg)
    else:
        return arg


def clipper():
    """amin funcitonality of the program is defined in this line"""
    ffmpeg_extract_subclip(args.targetname[0], args.start, args.end, targetname=args.destname)

def clipbyVideoFile():
    clip=VideoFileClip(args.targetname[0]).subclip(args.start,args.end)
    clip.write_videofile(args.destname)

def merger():

    clips=[]
    for i in range(len(args.targetname)):
        clips.append(VideoFileClip(args.targetname[i]))
        '''
        clip2 = VideoFileClip("blackvideo10sec.mp4").subclip(50, 60)
        clip3 = VideoFileClip("myvideo3.mp4")
        '''
    print(args.targetname)
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(args.destname)

def main():
    print(args.jobname)
    if args.jobname=='merge':
        print('inside ')
        merger()
    else:
        clipper()

main()



