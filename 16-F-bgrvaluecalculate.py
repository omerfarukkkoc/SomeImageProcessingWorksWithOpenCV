# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:00:54 2017

@author: omerf
"""

import cv2
import numpy as np


img = cv2.imread('sampleImages/frame0.jpg')
    
    
cv2.rectangle(img, (199,149), (201,151), (255,0,0), 2)
    
color = img[200, 150]
    
B = color[0]
G = color[1]
R = color[2]

print ('bgr')
print (B,G,R)

print ('hsv')

V = max(B,G,R)
S = ( V - min(B,G,R) ) / V
H = ( 240 + 60*(R - G) ) / ( V - min(B,G,R) )

print (H,S,V)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()