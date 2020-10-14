# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:52:02 2020

@author: Lucas Rocini
"""
import cv2

image = cv2.imread("E:\Workfolder\LearningOpenCVPython\image.jpg")

#tranform image to black
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        image[i][j] = (0,0,0)

font = cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(image, "255", (15,65), font, 2, (255,255,255), 2,)

cv2.putText(image, "70", (125,65), font, 2, (70,70,70), 2)

cv2.putText(image, "100", (225,65), font, 2, (100,100,100), 2)

cv2.putText(image, "1", (405,65), font, 2, (1,1,1), 2)

#tranform all different from true black into white
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] == 0:
            image[i][j] == (255,255,255)

#tranform all to black expect scale of 1 (black)
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        if image[i][j][0] == 1:
            image[i][j] == (255,255,255)
        else:
            image[i][j] == (0,0,0)

#show image and wait for the key
cv2.imshow("Window",image)
cv2.waitKey(0)

