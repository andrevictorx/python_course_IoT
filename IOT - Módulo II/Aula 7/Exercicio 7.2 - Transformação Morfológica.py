# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:01:33 2020

@author: T-Gamer
"""

import cv2
import numpy as np

img = np.zeros((150,150,3),np.uint8)
kernel = np.ones((5,5),np.uint8)

cv2.circle(img,(75,75),50,(255,255,255),thickness=10)
cv2.circle(img,(75,75),25,(255,255,255),thickness=10)
erosion = cv2.erode(img,kernel,iterations=1)
dilatation = cv2.dilate(img,kernel,iterations=1)


cv2.imshow('Original',img)
cv2.imshow('Erosion',erosion)
cv2.imshow('Dilatate',dilatation)


cv2.waitKey(0) &0xFF
cv2.destroyAllWindows()
