# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:04:03 2020

@author: T-Gamer
"""


import cv2
import numpy as np

# Criando imagem
img1 = np.zeros([512,512,3],np.uint8)

#Círculo
cv2.circle(img1,(75,75),50,(0,255,0),-1)

#Quadrado
cv2.rectangle(img1,(200,200),(300,300),(0,0,255),-1)

#Elipse
cv2.ellipse(img1,(431,431),(60,20),0,0,360,(255,0,0),-1)

#Mostrando imagem
cv2.imshow('imagem 1',img1)
tecla = cv2.waitKey(0) & 0xFF
cv2.destroyWindow('imagem 1')

img2 = np.zeros([512,512,3],np.uint8)
text = str(tecla)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img2,text,(100,300),font,5,(191,0,191),4,cv2.LINE_AA)
cv2.imshow('imagem 2',img2)
cv2.waitKey(1000) & 0xFF
cv2.destroyAllWindows()