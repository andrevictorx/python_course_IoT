# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:09:18 2020

@author: T-Gamer
"""
# Importar biblioteca
import cv2 

#Carregar as imagens
dog = cv2.imread('dog.jpg',cv2.IMREAD_COLOR)
dog_cinza = cv2.imread('dog.jpg',cv2.IMREAD_GRAYSCALE)
dog_transp = cv2.imread('dog.jpg',cv2.IMREAD_UNCHANGED)


#Mostrar as imagens
cv2.imshow('Janela 1',dog)
cv2.imshow('Janela 2',dog_cinza)
cv2.imshow('Janela 3',dog_transp)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

cv2.imshow('Nova Janela',dog)

