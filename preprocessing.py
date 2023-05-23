"""
Project: FootfallCam AI Evaluation Test
Created by: Teh Kuan Ting

This is the preprocessing script to prepare data for model training. 

Timestamp: v1.0 - 23/05/2022
"""
import pathlib
import cv2
import random
import os
import shutil

def vid2img():
    """
    Function: convert video to a folder of frame images
    Input: none
    Output: none
    """
    # video file path 
    vid_filepath = "./sample.mp4"
    # image folder path
    img_folderpath = "./data/tmp"
    pathlib.Path(img_folderpath).mkdir(parents=True, exist_ok=True)

    # capture video frame by frame
    capture = cv2.VideoCapture(vid_filepath)
    frame_num = 0

    while True:
        success, frame = capture.read()
        if not success: break
        # write the frame image
        cv2.imwrite(f'{img_folderpath}/frame_{frame_num}.jpg', frame)
        frame_num += 1

    capture.release()
    print("Done converting video to frame images!")
      
    
if __name__ == "__main__":
    vid2img()
