# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:05:45 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

cuttedImage = image[100:200, 100:200]

#show image and wait for the key
cv2.imshow("image",image)
cv2.imshow("cuttedImage",cuttedImage)
cv2.waitKey(0)






