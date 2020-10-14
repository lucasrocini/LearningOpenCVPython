# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 15:02:21 2020

@author: Lucas Rocini
"""

import cv2

image = cv2.imread("image.jpg")

font = cv2.FONT_HERSHEY_COMPLEX
#font = cv2.FONT_HERSHEY_PLAIN

cv2.putText(image, "Lucas", (50,50), font, 2, (255,255,255), 2, cv2.LINE_AA)

#show image and wait for the key
cv2.imshow("Window",image)
cv2.waitKey(0)