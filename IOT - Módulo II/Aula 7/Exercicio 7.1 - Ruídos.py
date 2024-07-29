# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:23:04 2020

@author: T-Gamer
"""

import cv2

img = cv2.imread('Flor.png')
median = cv2.medianBlur(img,9)
cv2.imshow('Original',img)
cv2.imshow('Filtrada',median)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()
