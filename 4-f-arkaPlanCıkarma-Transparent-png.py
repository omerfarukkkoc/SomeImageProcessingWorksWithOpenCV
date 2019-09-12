# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:01:42 2017

@author: omerf
"""

import cv2
import numpy as np

img2 = cv2.imread('sampleImages/mainlogo.png')


rows,cols,channels = img2.shape

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)


img2_fg = cv2.bitwise_and(img2,img2,mask = mask)


cv2.imshow('mask_inv',img2_fg)
cv2.imshow('res',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
