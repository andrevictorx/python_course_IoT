# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 09:19:15 2020

@author: T-Gamer
"""

import cv2
import matplotlib.pyplot as plt
img = cv2.imread('dog.jpg',0)
plt.figure(figsize=(30,8))

#Imagem original
plt.subplot(161)
plt.axis('off')
plt.imshow(img,cmap='gray')
plt.title('Original')

#Binário
#(image,threshold,maxValue,type)
ret, thresh1 = cv2.threshold(img,80,255,cv2.THRESH_BINARY)
plt.subplot(162)
plt.axis('off')
plt.imshow(thresh1,cmap='gray')
plt.title('Binário')

#Binário invertido
ret, thresh2 = cv2.threshold(img,80,255,cv2.THRESH_BINARY_INV)
plt.subplot(163)
plt.axis('off')
plt.imshow(thresh2,cmap='gray')
plt.title('Binário invertido')

#Truncado
ret, thresh3 = cv2.threshold(img,80,255,cv2.THRESH_TRUNC)
plt.subplot(164)
plt.axis('off')
plt.imshow(thresh3,cmap='gray')
plt.title('Truncado')

#Binarização to zero
ret, thresh4 = cv2.threshold(img,80,255,cv2.THRESH_TOZERO)
plt.subplot(165)
plt.axis('off')
plt.imshow(thresh4,cmap='gray')
plt.title('To zero')

#Binarização to zero inverso
ret, thresh5 = cv2.threshold(img,80,255,cv2.THRESH_TOZERO_INV)
plt.subplot(166)
plt.axis('off')
plt.imshow(thresh5,cmap='gray')
plt.title('Binário invertido')