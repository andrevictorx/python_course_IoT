# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:35:06 2020

@author: T-Gamer
"""

import cv2
import numpy as np

img = cv2.imread('love.jpg',0)
kernel = np.ones((5,5),np.uint8)

# Erode (image,kernel,interatrions=x)
# Apaga bordas
erosion = cv2.erode(img,kernel,iterations=1)

cv2.imshow('Original',img)
cv2.imshow('Filtrada',erosion)

cv2.waitKey(0) &0xFF
cv2.destroyAllWindows()