# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 22:54:26 2017

@author: omerf
"""

import sys
import numpy as np
import cv2
 
blue = 21
green = 53
red = 59  
 
color = np.uint8([[[blue, green, red]]])
hsv_color = cv2.cvtColor(color, cv2.COLOR_BGR2HSV)
 
#cv2.imshow('aa',color)
hue = hsv_color[0][0][0]
 
print("Lower bound is :"),
print("[" + str(hue-10) + ", 100, 100]\n")
 
print("Upper bound is :"),
print("[" + str(hue + 10) + ", 255, 255]")