# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:19:21 2020

@author: T-Gamer
"""
import cv2

img = cv2.imread('sal_pimenta.jpg')

# Kernel 3
median = cv2.medianBlur(img,5)
cv2.imshow('Original',img)
cv2.imshow('Filtrada',median)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

