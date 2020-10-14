# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:58:02 2020

@author: Lucas Rocini
"""


import cv2

image = cv2.imread("image.jpg")


#change to white color  in one pixel
image[0][0] = [255,255,255]
print(image[0][0])


#change to white color  in pixel sequence (square)
image[0:10,0:10] = [255,255,255]


#change to white color  in pixel sequence (all line)
image[0:10 , :] = [255,255,255]

#change to white color  in pixel sequence (all column)
image[ : ,0:10] = [255,255,255]


#show image and wait for the key
cv2.imshow("Window",image)
cv2.waitKey(0)



