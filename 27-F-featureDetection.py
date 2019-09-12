# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 15:53:05 2017

@author: omerf
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

import time

start = time.time()

img1 = cv2.imread('sampleImages/murattiFeatureMatchingSampleImage.jpg',0)
img2 = cv2.imread('sampleImages/murattiFeatureMatchingImage5.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10],None, flags=2)

"""
plt.imshow(img3)
plt.show()
"""
end = time.time()
print(start,end,end-start)
cv2.imshow('img3',img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
