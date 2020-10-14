# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:09:07 2020

@author: Lucas Rocini
"""
import cv2

image = cv2.imread("E:\Workfolder\LearningOpenCVPython\image.jpg")

#insert white dots on the image
for i in range (0, image.shape[0], 15):
    for j in range (0, image.shape[1], 15):
        image[i:i+3, j:j+3] = (255,255,255)

"""

# using AVERAGE
#blur on the image
image_blur = cv2.blur(image, (11,11))

#show image and wait for the key
cv2.imshow("original",image)
cv2.imshow("Window",image_blur)
cv2.waitKey(0)

"""

# using median
image_blur = cv2.medianBlur(image, 11)

#show image and wait for the key
cv2.imshow("original",image)
cv2.imshow("blur",image_blur)
cv2.waitKey(0)



