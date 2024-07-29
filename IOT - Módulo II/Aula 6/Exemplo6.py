# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 09:39:20 2020

@author: T-Gamer
"""

import cv2
#Carrega vídeo
cap = cv2.VideoCapture('video_car.avi')

#Codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')

#Vídeo de saída
output = cv2.VideoWriter('novo_video.avi',fourcc,20.0,(640,480))

#Salvar vídeo
while (cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame,0)
        #Escreve frames no vídeo de saída
        output.write(frame)
        #Mostrar vídeo na tela
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break
#Fecha janela
cap.release()
output.release()
cv2.destroyAllWindows()
