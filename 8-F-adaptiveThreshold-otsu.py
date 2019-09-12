# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:45:28 2017

@author: omerf
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 20:15:24 2017

@author: omerf
"""

import cv2
import numpy as np

img = cv2.imread('sampleImages/bookpage.jpg')

grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
 
retval2 , threshold2 = cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print (retval2)
cv2.imshow('original',img)
cv2.imshow('Otsu threshold',threshold2)

cv2.waitKey(0)
cv2.destroyAllWindows()