# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:16:03 2020

@author: T-Gamer
"""


import cv2

img = cv2.imread('ruido.jpg')

# Kernel 7x7
gauss = cv2.GaussianBlur(img,(7,7),0)

cv2.imshow('Original',img)
cv2.imshow('Filtrada',gauss)

cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()