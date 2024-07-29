# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:32:23 2020

@author: T-Gamer
"""
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('shadow_book.png',0)
plt.figure(figsize=(20,8))

#Binário
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)

#Métodos Adaptativos
#(image,maxValue,adaptiveMethod,thesholdType,blockSize,constant)
thresh_adapt1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY,11,2)
thresh_adapt2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY,11,2)
    
#Visualização
plt.subplot(141)
plt.axis('off')
plt.imshow(img,cmap='gray')
plt.title('Original')

plt.subplot(142)
plt.axis('off')
plt.imshow(thresh1,cmap='gray')
plt.title('Binário')

plt.subplot(143)
plt.axis('off')
plt.imshow(thresh_adapt1,cmap='gray')
plt.title('Média')

plt.subplot(144)
plt.axis('off')
plt.imshow(thresh_adapt2,cmap='gray')
plt.title('Gaussiano')