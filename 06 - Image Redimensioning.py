# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:09:59 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

width = image.shape[1]
height = image.shape[0]
proportion = float(height/width)

newWidth = 150
newHeight = int(newWidth*proportion)

"""
#direct conversion
newWidth = 100
newHeight = 100
"""

image = cv2.resize(image, (newWidth, newHeight))

#show image and wait for the key
cv2.imshow("image",image)
cv2.waitKey(0)
