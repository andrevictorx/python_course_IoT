# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:54:09 2020

@author: André
"""
import cv2
import numpy as np

def function(event,x,y,flags,param):
    if event == cv2.EVENT_MOUSEWHEEL:
        cv2.circle(img,(x,y),50,(255,0,0),-1)
    elif event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.ellipse(img,(x,y),(60,20),0,0,360,(0,255,0),-1)

img = np.zeros((512,512,3),np.uint8)

cv2.namedWindow('Window')

cv2.setMouseCallback('Window',function)

while True:
    cv2.imshow('Window',img)
    if cv2.waitKey(20) & 0xFF == 27:#Esc
        break
#Close window
cv2.destroyAllWindows()
                   
