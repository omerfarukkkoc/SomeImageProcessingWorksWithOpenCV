# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 17:00:05 2017

@author: omerf
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('sampleImages/1.jpg',cv2.IMREAD_GRAYSCALE)

#plt.xticks([]), plt.yticks([])     #cetvel
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50,200], [80,200], 'b', linewidth=4) 
plt.show()

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

