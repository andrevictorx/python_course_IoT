# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:24:01 2020

@author: T-Gamer
"""
import cv2
import numpy as np
img = np.ones([240,360,3],np.uint8)*255
text = "André"
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,text,(90,120),font,1.5,(191,0,191),4,cv2.LINE_AA)
cv2.imshow('imagem',img)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()


