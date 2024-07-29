# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:40:50 2020

@author: T-Gamer
"""
import cv2
# Leitura de vídeo
cap = cv2.VideoCapture('video_car.avi')
fourcc = cv2.VideoWriter_fourcc(*'XVID')#Extensão do vídeo
# Cria vídeo
output = cv2.VideoWriter('carros_psicodelicos.avi',fourcc,30.0,(300,300))
#Enquanto o vídeo estiver aberto
while (cap.isOpened()):
    #Leia os frames desse vídeo
    ret, frame = cap.read()
    #Se o vídeo for aberto corretamente
    if ret == True:
        #Converta os frames para HSV
        frame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        #Ajuste o tamanho dos frames à resolução do vídeo
        frame = cv2.resize(frame,(300,300))
        #Escreve frames no vídeo de saída
        output.write(frame)
        #Mostrar vídeo na tela
        cv2.imshow('carros_psicodelicos.avih',frame)
        #Se Q for pressionado, saia do vídeo
        if (cv2.waitKey(1) & 0xFF == ord('q')):
            break
    #Se o vídeo NÃO for aberto corretamente, saia do vídeo
    else:
        break
#Fecha janela
cap.release()
output.release()
cv2.destroyAllWindows()
