# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 11:44:16 2020

@author: André
"""

import cv2
import numpy as np
image_path = "./images.jpg"
min_confidence = 0.35

model_proto_path = "./MobileNetSSD_deploy.prototxt"
model_binary_path = "./MobileNetSSD_deploy.caffemodel"

classes = ['backgroun', 'aeroplane','bicycle','bird','boat',
           'bottle','bus','car','cat','chair','cow','diningtable',
           'dog','horse','motorbike','person','pottedplant','sheep',
           'sofa','train','tvmonitor']

colors = np.random.uniform(0,255, size=(len(classes),3))

print('[INFO] loading model...')
net = cv2.dnn.readNetFromCaffe(model_proto_path, model_binary_path)

image = cv2.imread(image_path)
(h,w) = image.shape[:2]
blob = cv2.dnn.blobFromImage(cv2.resize(image,(300,300)),0.007843,(300,300),127.5)
print('[INFO] computing object detections...')
net.setInput(blob)
detections = net.forward()

for i in np.arange(0,detections.shape[2]):
    confidence = detections[0,0,i,2]
    if confidence>min_confidence:
        idx = int(detections[0,0,i,1])
        box = detections[0,0,i,3:7]*np.array([w,h,w,h])
        (startX, startY,endX,endY) = box.astype('int')
        label = '{}: {:.2f}%'.format(classes[idx],confidence*100)
        print('[INFO] {}'.format(label))
        cv2.rectangle(image, (startX,startY), (endX,endY), colors[idx], 2)
        y = startY -15 if startY-15>15 else startY+15
        cv2.putText(image,label,(startX,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,colors[idx],2)
cv2.imshow('Output',image)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

