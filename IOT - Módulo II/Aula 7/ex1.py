# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 08:11:18 2020

@author: T-Gamer
"""

import cv2

# Kernel 5x5
#Carrega img
img = cv2.imread('ruido.jpg')
# Aplica o filtro
blur = cv2.blur(img,(5,5))
# Mostra imagem
cv2.imshow('Filtrada',blur)
cv2.imshow('Original',img)
# Fecha janela
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()