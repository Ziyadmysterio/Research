import cv2
import numpy as np
import time
start_time = time.time()

def LBP_Value(img, centerPixel, x, y):
    LbpVal = 0
    try:
        if img[x][y] >= centerPixel:
            LbpVal = 1
    except:
        pass
    return LbpVal

def lbp_calculated_pixel(img, x, y):
    centerPixel = img[x][y]
    LBP_array = []
      
    # top_left
    LBP_array.append(LBP_Value(img, centerPixel, x-1, y-1))
      
    # top
    LBP_array.append(LBP_Value(img, centerPixel, x-1, y))
      
    # top_right
    LBP_array.append(LBP_Value(img, centerPixel, x-1, y + 1))
      
    # right
    LBP_array.append(LBP_Value(img, centerPixel, x, y + 1))
      
    # bottom_right
    LBP_array.append(LBP_Value(img, centerPixel, x + 1, y + 1))
      
    # bottom
    LBP_array.append(LBP_Value(img, centerPixel, x + 1, y))
      
    # bottom_left
    LBP_array.append(LBP_Value(img, centerPixel, x + 1, y-1))
      
    # left
    LBP_array.append(LBP_Value(img, centerPixel, x, y-1))
       
    # Now, we need to convert binary
    # values to decimal
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
   
    val = 0
      
    for i in range(len(LBP_array)):
        val += LBP_array[i] * power_val[i]
          
    return val
   

img1=cv2.imread('Code/Research/test.jpg')
img=cv2.resize(img1, [224,224], interpolation = cv2.INTER_AREA)
height,width,channel=img.shape
img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_lbp = np.zeros((height, width,3), np.uint8)
for i in range(0, height):
    for j in range(0, width):
         img_lbp[i, j] = lbp_calculated_pixel(img_gray, i, j)
hist_lbp = cv2.calcHist([img_lbp], [0], None, [255], [0, 255])

print("--- %s seconds ---" % (time.time() - start_time))