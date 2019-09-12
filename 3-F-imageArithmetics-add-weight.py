# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 19:16:12 2017

@author: omerf
"""

import cv2
import numpy as np

img1 = cv2.imread('sampleImages/3D-Matplotlib.png')
img2 = cv2.imread('sampleImages/mainsvmimage.png')

add = img1+img2

weighted = cv2.addWeighted(img1, 0.9, img2, 0.1, 0)
weighted1 = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imshow('add',add)

cv2.imshow('weihted', weighted)

cv2.imshow('weihted1', weighted1)
cv2.waitKey(0)
cv2.destroyAllWindows()