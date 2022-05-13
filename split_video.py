import sys
import argparse

from os import listdir
from os.path import isfile

from pathlib import Path

import cv2

def video_to_frames(pathIn, pathOut):
    Path(f"{pathOut}").mkdir(parents=True, exist_ok=True)
    f = 0
    vidcap = cv2.VideoCapture(pathIn)
    if vidcap.isOpened():
        success,image = vidcap.read()
        while success:
            vidcap.set(cv2.CAP_PROP_POS_MSEC,(f*1000))
            success,image = vidcap.read()
            if success:
                cv2.imwrite( f"{pathOut}/frame{f}.jpg", image)
                f += 1

def get_data(pathIn):
    folders_root = [f for f in listdir(pathIn)]
    for fr in folders_root:
        files = [f for f in listdir(f"{pathIn}/{fr}") if isfile(f"{pathIn}/{fr}/{f}")]
        for f in files:
            print(f"{pathIn}/{fr}/{f}")
            video_to_frames(f"{pathIn}/{fr}/{f}", f"{pathIn}/{fr}/frames_{f[:f.index('.avi')]}")


if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("--pathIn", help="repertoire des videos")
    args = a.parse_args()
    
    get_data(args.pathIn)
