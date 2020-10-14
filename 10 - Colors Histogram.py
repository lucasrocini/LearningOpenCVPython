# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 16:09:07 2020

@author: Lucas Rocini
"""
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("E:\Workfolder\LearningOpenCVPython\image.jpg")
blueList = []
greenList = []
redList = []

blueResult = []
greenResult = []
redResult = []

#split and creation of list for every color
for i in range(0, image.shape[0]):
    for j in range(0, image.shape[1]):
        blueList.append(image[i][j][0])
        greenList.append(image[i][j][1])
        redList.append(image[i][j][2])

#list with all existing numbers (not repeated)
notRepeatedBlueList = sorted(set(blueList))
notRepeatedGreenList = sorted(set(greenList))
notRepeatedRedList = sorted(set(redList))

#Summation of quantity for each color scale
for i in range(0, len(notRepeatedBlueList)):
    summation = 0
    for j in range(0, len(blueList)):
        if notRepeatedBlueList[i] == blueList[j]:
            summation +=1
    blueResult.append(summation)

for i in range(0, len(notRepeatedGreenList)):
    summation = 0
    for j in range(0, len(greenList)):
        if notRepeatedGreenList[i] == greenList[j]:
            summation +=1
    greenResult.append(summation)

for i in range(0, len(notRepeatedRedList)):
    summation = 0
    for j in range(0, len(redList)):
        if notRepeatedRedList[i] == redList[j]:
            summation +=1
    redResult.append(summation)

plt.plot(blueResult, color="blue")
plt.plot(greenResult, color="green")
plt.plot(redResult, color="red")
plt.show

print(blueList)
print(notRepeatedBlueList)

#show image and wait for the key
cv2.imshow("Window",image)
cv2.waitKey(0)


