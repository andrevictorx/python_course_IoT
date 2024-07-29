# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:06:26 2020

@author: T-Gamer
"""
import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'XVID')
output = cv2.VideoWriter('exercício 6.2.avi',fourcc,30.0,(640,480))
back_color = (140,100,40)
color = (0,0,0)

for _ in range(20):
    x = np.random.randint(0,640)
    y = np.random.randint(0,480)
    for i in range(15):
        frame = np.full((480,640,3),back_color,dtype=np.uint8)
        circ = cv2.circle(frame,(x,y),50,color,-1)
        output.write(frame)
        cv2.imshow('Exercicio 6.2',frame)
        cv2.waitKey(10)
        
output.release()
cv2.destroyAllWindows()
