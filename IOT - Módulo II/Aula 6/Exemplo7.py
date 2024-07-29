# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:15:47 2020

@author: T-Gamer
"""


import cv2
img = cv2.imread('dog.jpg')
img_hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Original',img)
cv2.imshow('HSV',img_hsv)
cv2.imshow('Gray',img_gray)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()