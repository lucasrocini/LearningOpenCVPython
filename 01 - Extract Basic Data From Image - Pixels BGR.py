# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:18:40 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

#show image and wait for the key
cv2.imshow("Image",image)
cv2.waitKey(0)

#return height from the image (pixels)
print(image.shape[0])

#return width from the image (pixels)
print(image.shape[1])

#return color channels
print(image.shape[2])


#show each value BGR from each pixel
print(image)

#show all pixels BGR values
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        #print all
        print(image[i][j])
        """
        #print each color in one line
        for h in range(0,3):
            #print(image[i][j][h])
        """



