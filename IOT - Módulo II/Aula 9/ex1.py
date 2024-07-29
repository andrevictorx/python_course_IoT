# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 08:50:36 2020

@author: André
"""

import time 
import cv2
import numpy as np

image_path ="./dog.jpg"
labels_path = "./synset_words.txt"
model_proto_path = "./bvlc_googlenet.prototxt"
model_binary_path = "./bvlc_googlenet.caffemodel"

image = cv2.imread(image_path)
rows = open(labels_path).read().strip().split("\n")

classes = []
for row in rows:
    classes = [row[row.find(' ')+ 1:].split(",")[0]]
    
blob = cv2.dnn.blobFromImage(image, 1, (224,224),(104,117,123))
    
net = cv2.dnn.readNetFromCaffe(model_proto_path, model_binary_path)

start = time.time()
net.setInput(blob)
preds = net.forward()
end = time.time()
print("[INFO] classification took {:.5} seconds".format(end - start))
