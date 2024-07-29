# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:55:52 2020

@author: T-Gamer
"""

import cv2

#Kernel retangular
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
print(rect_kernel)
print('\n')
#Kernel Elíptica
ellipse_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
print(ellipse_kernel)
print('\n')
#Kernel tipo Cruz
cross_kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
print(cross_kernel)

