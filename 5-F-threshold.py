# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:15:24 2017

@author: omerf
"""

import cv2
import numpy as np

img = cv2.imread('sampleImages/bookpage.jpg')
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval, threshold = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
print (retval)

th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 3)
cv2.imshow('original',img)
cv2.imshow('Adaptive threshold',th)

cv2.imshow('threshold',threshold)


cv2.waitKey(0)
cv2.destroyAllWindows()