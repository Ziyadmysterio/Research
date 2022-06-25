import cv2
import numpy as np

import time
start_time = time.time()

image_file = "Code/Research/test.jpg"
img_bgr = cv2.imread(image_file)
img1=cv2.resize(img_bgr, [224,224], interpolation = cv2.INTER_AREA)
height, width,channel = img1.shape
img_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)    
LBP_value = np.zeros((height, width,3), np.uint8)

for i in range(1, height-1):
    for j in range(1, width-1):
        if(img_gray[i-1][j-1]>img_gray[i][j]):
            LBP_value[i-1][j-1]=1
        
        if(img_gray[i-1][j]>img_gray[i][j]):
            LBP_value[i-1][j]=128

        if(img_gray[i-1][j+1]>img_gray[i][j]):
            LBP_value[i-1][j+1]=64
        
        if(img_gray[i][j+1]>img_gray[i][j]):
            LBP_value[i][j+1]=32

        if(img_gray[i+1][j+1]>img_gray[i][j]):
            LBP_value[i+1][j+1]=16

        if(img_gray[i+1][ j]>img_gray[i][j]):
            LBP_value[i+1][j]=8

        if(img_gray[i+1][ j-1]>img_gray[i][j]):
            LBP_value[i+1][j-1]=4

        if(img_gray[i][ j-1]>img_gray[i][j]):
            LBP_value[i][j-1]=2

        LBP_value[i][j] = LBP_value[i-1][j-1]+LBP_value[i-1][j]+LBP_value[i-1][j+1]+LBP_value[i][j+1]+LBP_value[i+1][j+1]+LBP_value[i+1][j]+LBP_value[i+1][j-1]+LBP_value[i][j-1]

             #img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
    
hist_lbp = cv2.calcHist([LBP_value], [0], None, [255], [0, 255])

print("--- %s seconds ---" % (time.time() - start_time))