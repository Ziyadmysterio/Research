import cv2
import numpy as np
import os
import lbp
from matplotlib import pyplot as plt
import pandas as pd

video_path = "C:/Users/ziyad/Desktop/all desktop/Heriotwat/RP/Code/Research/video1.mp4"
dir_name="C:/Users/ziyad/Desktop/all desktop/Heriotwat/RP/Code/Research/testvid"
p_frame_thresh = 200000 # You may need to adjust this threshold
dfn=list()
df=list()
cap = cv2.VideoCapture(video_path)
# Read the first frame.
ret, prev_frame = cap.read()
count=0
while ret:
    ret, curr_frame = cap.read()

    if ret:
        diff = cv2.absdiff(curr_frame, prev_frame)
        non_zero_count = np.count_nonzero(diff)
        if non_zero_count > p_frame_thresh:
            name='rec_frame'+str(count)+'.jpg'
            height, width, _ = prev_frame.shape
            img_gray = cv2.cvtColor(prev_frame,
                        cv2.COLOR_BGR2GRAY)
            img_lbp = np.zeros((height, width),
                   np.uint8)
            for i in range(0, height):
                for j in range(0, width):
                    img_lbp[i, j] = lbp.lbp_calculated_pixel(img_gray, i, j)
            dfn=[prev_frame,img_lbp]
            df.append(dfn)
            
        prev_frame = curr_frame
        
        count+=1
        cv2.waitKey(1)


