# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:25:51 2020

@author: T-Gamer
"""

import cv2
import numpy as np
import random

def function(event,x,y,flags,param):
    global b,g,r
    if event == cv2.EVENT_LBUTTONDOWN:
        b = random.randint(0,255)
        g = random.randint(0,255) 
        r = random.randint(0,255)

#Channels
#Black window
b = 0
g = 0
r = 0

#New window
cv2.namedWindow('Window')

#Mouse Callback
cv2.setMouseCallback('Window',function)

while True:
    img = np.full((512,512,3),(b,g,r),np.uint8)
    cv2.imshow('Window',img)
    if cv2.waitKey(1) & 0xFF == 27:#Esc
        break
#Close window
cv2.destroyAllWindows()