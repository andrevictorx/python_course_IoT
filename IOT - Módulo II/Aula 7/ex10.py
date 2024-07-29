# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 10:08:29 2020

@author: T-Gamer
"""

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('shadow_book.png',0)
#([image],[channels],[mask],[histSize],[range])
hist = cv2.calcHist([img],[0],None,[256],[0,256])

#(array,bins,range)
plt.hist(img.ravel(),256,[0,256])
plt.show()
