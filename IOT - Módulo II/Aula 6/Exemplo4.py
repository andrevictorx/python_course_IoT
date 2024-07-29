# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:28:30 2020

@author: T-Gamer
"""
import cv2

# Carrega o vídeo
cap = cv2.VideoCapture('video_car.avi')

#Lê frames
ret, frame = cap.read()

while(True):
    ret,frame = cap.read()
    if ret == False:
        break
    cv2.imshow('Corrida',frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
#Fecha janela
cap.release()
cv2.destroyAllWindows()
