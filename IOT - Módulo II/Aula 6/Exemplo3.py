# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:58:01 2020

@author: T-Gamer
"""
import cv2
import numpy as np

#Criar Imagem
img = np.zeros((512,512,3),np.uint8)

text = 'Tabuleiro Maneiro'
font = cv2.FONT_HERSHEY_SIMPLEX

# Escrevendo na imagem
#(image,texto,(xi,yi),font,fontsize,color,thickness,linetype)
cv2.putText(img,text,(50,500),font,1.5,(191,0,191),4,cv2.LINE_AA)

#Mostrar a imagem
cv2.imshow('imagem',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()