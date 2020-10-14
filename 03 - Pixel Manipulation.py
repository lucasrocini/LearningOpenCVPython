# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:04:41 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

#tuple to represent white
white = (255,255,255)
"""
#transform all pixels to white
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        image[i][j] = white

#transform each 10 pixels to white
for i in range(0, image.shape[0], 10):
    for j in range(0, image.shape[1], 10):
        image[i][j] = white
        
#transform each line pixels to white
for i in range(0, image.shape[0], 10):
    for j in range(0, image.shape[1]):
        image[i][j] = white

# draw white squares
for i in range(0, image.shape[0],20):
    for j in range(0, image.shape[1],20):
        image[i:i+5, j:j+5] = white
"""
# draw white on blue
for i in range(0, image.shape[0],20):
    for j in range(0, image.shape[1],20):
        if image[i][j][0] == 255:  #blue (openCV works with BGR and not RGB)
            image[i][j] = branco


#show image and wait for the key
cv2.imshow("Window",image)
cv2.waitKey(0)
