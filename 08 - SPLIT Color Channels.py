# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:20:59 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

#tuple to split
(b,g,r) = cv2.split(image)


cv2.imshow("image",image)
cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)

#wait for the key
cv2.waitKey(0)




