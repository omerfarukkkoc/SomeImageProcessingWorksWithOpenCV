# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:54:38 2016

@author: omerfarukkoc
"""

import cv2
import numpy as np
import sys

def nothing(x):
    pass
	
	
hueMin = 179 
saturationMin = valueMin = 0
hueMax = saturationMax = valueMax = 255

cv2.namedWindow('Renk Ayar Penceresi')
cv2.createTrackbar('H-Min', 'Renk Ayar Penceresi', 0, 179, nothing)
cv2.createTrackbar('S-Min', 'Renk Ayar Penceresi', 0, 255, nothing)
cv2.createTrackbar('V-Min', 'Renk Ayar Penceresi', 0, 255, nothing)
cv2.createTrackbar('H-Max', 'Renk Ayar Penceresi', 0, 255, nothing)
cv2.createTrackbar('S-Max', 'Renk Ayar Penceresi', 0, 255, nothing)
cv2.createTrackbar('V-Max', 'Renk Ayar Penceresi', 0, 255, nothing)

cv2.setTrackbarPos('H-Min', 'Renk Ayar Penceresi', hueMin)
cv2.setTrackbarPos('S-Min', 'Renk Ayar Penceresi', saturationMin)
cv2.setTrackbarPos('V-Min', 'Renk Ayar Penceresi', valueMin)
cv2.setTrackbarPos('H-Max', 'Renk Ayar Penceresi', hueMax)
cv2.setTrackbarPos('S-Max', 'Renk Ayar Penceresi', saturationMax)
cv2.setTrackbarPos('V-Max', 'Renk Ayar Penceresi', valueMax)
	
cap = cv2.VideoCapture(0)


if cap.isOpened()==True: 
    print ('Kamera Açıldı')
        
else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)


while(1):
        
        try:
            start = time.time()
            ret, frame = cap.read()
    
            if ret != True:
                print ('HATA!! Frame Alınamıyor \nYeniden Başlatın')
                cv2.destroyAllWindows()
                cap.release()
                break
                exit(1)
    
			frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
			hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
			
			cv2.rectangle(frame, (199,149), (201,151), (255,0,0), 2)
			#lower = np.array([38, 153, 236])
			#upper = np.array([255, 255, 255])
			
			lower = np.array([110, 50, 50])
			upper = np.array([130, 255, 255])
			
			mask = cv2.inRange(hsv, lower, upper)
			res = cv2.bitwise_and(frame,frame, mask= mask)
			
			cv2.imshow('frame',frame)
			#cv2.imshow('hsv',hsv)
			cv2.imshow('mask',mask)
			cv2.imshow('res',res)
			
			
		    k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break
              
             
        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise

cv2.destroyAllWindows()
cap.release()