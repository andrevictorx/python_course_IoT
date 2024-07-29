# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:34:33 2020

@author: T-Gamer
"""
import cv2

#Carrega vídeo
cap = cv2.VideoCapture('video_car.avi')

while(cap.isOpened()):
    ret, frame = cap.read()
    if cv2.waitKey(1) == ord('q') or ret == False:
        break
    cv2.imshow('frame',frame)

#Fechando vídeo

cap.release()
cv2.destroyAllWindows()
