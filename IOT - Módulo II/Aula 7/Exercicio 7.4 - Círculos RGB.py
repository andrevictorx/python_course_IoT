# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:23:16 2020

@author: André
"""

import cv2
import numpy as np

b = 0
g = 0
r = 0    

font = cv2.FONT_HERSHEY_SIMPLEX

def function(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),20,(b,g,r),-1)


img = np.zeros((512,512,3),np.uint8)
cv2.namedWindow('Window')
cv2.setMouseCallback('Window',function)


while True:
    cv2.putText(img,'red = '+str(r),(20,30),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'green='+str(g),(20,60),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.putText(img,'blue = '+str(b),(20,90),font,1,(255,255,255),2,cv2.LINE_AA)
    cv2.imshow('Window',img)
    key = cv2.waitKey(10) & 0xFF

    
    if key == ord('b'):
        b+=10
        cv2.rectangle(img,(0,50),(200,100),(0,0,0),-1)
        if b>255:
            b=0
        
    elif key == ord('g'):
        g+=10
        cv2.rectangle(img,(0,30),(200,80),(0,0,0),-1)
        if g>255:
            g=0
        
    elif key == ord('r'):
        r+=10
        cv2.rectangle(img,(0,0),(200,40),(0,0,0),-1)
        if r>255:
            r=0
    
    if key == ord('x'):
        break
#Close window
cv2.destroyAllWindows()
    