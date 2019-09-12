# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:42:47 2017

@author: omerf
"""

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('sampleImages/opencv-python-foreground-extraction-tutorial.jpg')
mask = np.zeros(img.shape[:2],np.uint8)

bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)

rect =(161,79,150,150)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask==0)|(mask==2),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

#Vcv2.imshow('mask',mask)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""
plt.imshow(img)
plt.colorbar()
plt.show()
"""