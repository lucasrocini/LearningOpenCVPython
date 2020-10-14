# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:09:07 2020

@author: Lucas Rocini
"""
import numpy as np
import cv2

image = cv2.imread("E:\Workfolder\LearningOpenCVPython\image.jpg")

darkBlue = np.array([100,67,0], dtype="uint8")
lightBlue = np.array([255,128,50], dtype="uint8")

#ipen camera
camera = cv2.VideoCapture(0)

while True:
    (success, frame) = camera.read()
    
    if not success:
        break
    
    #trehshold (paints white the blue range)
    obj = cv2.inRange(frame, darkBlue, lightBlue)
    
    (outlines, _) = cv2.findContours(obj.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    if len(outlines) > 0:
        outlines = sorted(outlines, key=cv2.contourArea, reverse=True)[0]
    
        rectangle = np.int32(cv2.boxPoints(cv2.minAreaRect(outlines)))
        
        cv2.drawContours(frame, [rectangle], -1, (0,255,255), 2)
        
    cv2.imshow("Janela", frame)
    cv2.imshow("Janela1", obj)
    
    if cv2.waitKey(1) & 0xFF == ord("s"):
        break


camera.release()
cv2.destroyAllWindows()


