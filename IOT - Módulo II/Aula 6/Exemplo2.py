# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 08:32:25 2020

@author: T-Gamer
"""


import cv2
import numpy as np

#Criando imagem
img = np.zeros((512,512,3),np.uint8)

# Linhas verticais
#(image,(xi,yi),(xf,yf),(color),thickness)
cv2.line(img,(150,0),(150,512),(255,255,255),5)
cv2.line(img,(350,0),(350,512),(255,255,255),5)

# Linhas horizontias
cv2.line(img,(0,150),(512,150),(255,255,255),5)
cv2.line(img,(0,350),(512,350),(255,255,255),5)

# Retângulo
#(image,(xi,yi),(xf,yf),(color),thickness)
cv2.rectangle(img,(200,200),(300,300),(0,255,0),-1)

# Círculo
#(image,(xc,yc),(radius),(color),thickness)
cv2.circle(img,(75,75), 50,(0,0,255),-1)

# Elipse
# (image,(xc,yc),(axes),angle,startAngle,endangle,color,thickness)
cv2.ellipse(img,(430,430),(60,20),0,0,360,(255,0,0),-1)

# Polígono
pts = np.array([[431,10],[390,120],[471,120],[431,10]],np.int32)
pts = pts.reshape((-1,1,2))
#(image,(coord),boolean,(color),tickness)
cv2.polylines(img,[pts],True,(0,255,255),8)

# Mostrar imagem
cv2.imshow('tic-tac-toe',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

