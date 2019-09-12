# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 17:14:53 2017

@author: omerf
"""

import cv2

img = cv2.imread('sampleImages/muratti.jpg',0)
# Initiate ORB detector
orb = cv2.ORB_create()
# find the keypoints with ORB
kp = orb.detect(img,None)
# compute the descriptors with ORB
kp, des = orb.compute(img, kp)
# draw only keypoints location,not size and orientation
img2 = cv2.drawKeypoints(img, kp, None, color=(255,0,0), flags=0)


#plt.imshow(img2), plt.show()


cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
