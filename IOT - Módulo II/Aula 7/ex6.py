# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:44:10 2020

@author: T-Gamer
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('love.jpg',0)
kernel = np.ones((5,5),np.uint8)

# Opening (image,morphType,kernel)
opening = cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)

# Closing (image,morphtype,kernel)
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)

# Gradient
gradient = cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)

# Visualização MATPLOTLIB
plt.figure(figsize=(20,8))
plt.subplot(141)
plt.axis('off')
plt.imshow(img,cmap='gray')
plt.title('Original')

plt.figure(figsize=(20,8))
plt.subplot(142)
plt.axis('off')
plt.imshow(opening,cmap='gray')
plt.title('Opening')

plt.figure(figsize=(20,8))
plt.subplot(143)
plt.axis('off')
plt.imshow(closing,cmap='gray')
plt.title('Closing')

plt.figure(figsize=(20,8))
plt.subplot(144)
plt.axis('off')
plt.imshow(gradient,cmap='gray')
plt.title('Gradient')