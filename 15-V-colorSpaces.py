# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:23:15 2017

@author: omerf
"""

import cv2

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
    
    
    RGB2BGR = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    frame *= 1./255;
    RGB2BGR1 = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR1)
    
    HSV2BGR_FULL = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR_FULL)
    
    BGR2YUV = cv2.cvtColor(frame, cv2.COLOR_BGR2YUV)
    
    BGR2HLS = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)
    
    BGR2LAB = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    
    BGR2RGBA = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    
    BGR2XYZ = cv2.cvtColor(frame, cv2.COLOR_BGR2XYZ)
    
    
    
    cv2.imshow('Original',frame)
    #cv2.imshow('hsv',hsv)
    cv2.imshow('RGB2BGR',RGB2BGR)
    cv2.imshow('RGB2BGR1',RGB2BGR1)
    cv2.imshow('HSV2BGR_FULL',HSV2BGR_FULL)
    cv2.imshow('BGR2YUV',BGR2YUV)
    cv2.imshow('BGR2HLS',BGR2HLS)
    cv2.imshow('BGR2LAB',BGR2LAB)
    cv2.imshow('BGR2RGBA',BGR2RGBA)
    cv2.imshow('BGR2XYZ',BGR2XYZ)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()