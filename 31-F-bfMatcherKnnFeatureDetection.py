# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 17:25:53 2017

@author: omerf
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt
import time

start = time.time()
img1 = cv2.imread('sampleImages/murattiFeatureMatchingSampleImage.jpg',0)
img2 = cv2.imread('sampleImages/murattiFeatureMatchingImage5.jpg',0)

# Initiate SIFT detector
#sift = cv2.SIFT()

sift = cv2.xfeatures2d.SIFT_create()

# find the keypoints and descriptors with SIFT
kp1, des1 = sift.detectAndCompute(img1,None)
kp2, des2 = sift.detectAndCompute(img2,None)

# BFMatcher with default params
bf = cv2.BFMatcher()
matches = bf.knnMatch(des1,des2, k=2)

# Apply ratio test
good = []
for m,n in matches:
    if m.distance < 0.75*n.distance:
        good.append([m])

# cv2.drawMatchesKnn expects list of lists as matches.
img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
end = time.time()
print(start,end,end-start)
#plt.imshow(img3),plt.show()



cv2.imshow('img3',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
