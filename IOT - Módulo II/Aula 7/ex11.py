# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:15:15 2020

@author: T-Gamer
"""

import cv2

img = cv2.imread('shadow_book.png',0)

# Binarização
# (image,theshold,maxValue,type)
ret, thresh1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
ret, thresh_otsu = cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Original',img)
cv2.imshow('Binary',thresh1)
cv2.imshow('Otsu',thresh_otsu)
cv2.waitKey(0) &0xFF
cv2.destroyAllWindows()
