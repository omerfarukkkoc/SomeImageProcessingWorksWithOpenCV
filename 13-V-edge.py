# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 16:51:02 2017

@author: omerf
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 15:48:54 2017

@author: omerf
"""

import cv2
#import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()
    #frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    edges = cv2.Canny(frame,50,100)
    cv2.imshow('frame',frame)
    cv2.imshow('Edges',edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()