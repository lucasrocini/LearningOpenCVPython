# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:15:01 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

#invert the pixels order on X axis
rotatedImage = image[:, ::-1]

#invert the pixels order on Y axis
rotatedImage = image[::-1, :]

#invert the pixels order on X and Y axis
rotatedImage = image[::-1, ::-1]

#show image and wait for the key
cv2.imshow("image",image)
cv2.imshow("rotatedImage",rotatedImage)
cv2.waitKey(0)


