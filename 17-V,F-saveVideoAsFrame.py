# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:04:29 2017

@author: omerf
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):
    _, frame = cap.read()
    
    frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
    count = 0
    cv2.imwrite("frame%d.jpg" % count, frame)
    count = count+1
    break

cap.release()
cv2.destroyAllWindows()
