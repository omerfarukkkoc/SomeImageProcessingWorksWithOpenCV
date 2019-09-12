# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 23:42:27 2017

@author: omerf
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #lower = np.array([106, 100, 100])
    lower = np.array([60, 100, 50])
    upper = np.array([255, 255, 255])
    
    mask = cv2.inRange(hsv, lower, upper)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    kernel = np.ones((3,3),np.uint8)
    
    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('Opening',opening)
    cv2.imshow('Closing',closing)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()