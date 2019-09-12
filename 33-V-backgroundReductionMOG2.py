# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 14:42:21 2017

@author: omerf
"""

import cv2
import numpy as np
import sys
import time

fps = 0

#cap = cv2.VideoCapture('sampleVideos/people-walking.mp4')

#cap = cv2.VideoCapture('sampleVideos/768x576.avi')

cap = cv2.VideoCapture(0)
cap1 = cv2.VideoCapture(1)


fgbg = cv2.createBackgroundSubtractorMOG2()
fgbg1 = cv2.createBackgroundSubtractorMOG2()


if cap.isOpened()==True: 
    print ('Kamera Açıldı')
        
else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)

frame_count = 0
while(1):
        
        try:
            start = time.time()
            ret, frame = cap.read()
            ret1, frame1 = cap1.read()

            if ret != True:
                print ('HATA!! Frame Alınamıyor \nYeniden Başlatın')
                cv2.destroyAllWindows()
                cap.release()
                break
                exit(1)
            
            fgmask = fgbg.apply(frame)
            fgmask1 = fgbg1.apply(frame1)

            fgmask = cv2.resize(fgmask, (400, 300),interpolation=cv2.INTER_LINEAR)
            fgmask1 = cv2.resize(fgmask1, (400, 300),interpolation=cv2.INTER_LINEAR)
            frame = cv2.resize(frame, (400, 300),interpolation=cv2.INTER_LINEAR)
            frame1 = cv2.resize(frame1, (400, 300),interpolation=cv2.INTER_LINEAR)

            cv2.imshow('fgmask',fgmask)
            cv2.imshow('fgmask1',fgmask1)

            
            # cv2.putText(frame, "Fps: "+str(fps), (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            # cv2.imwrite("imgs/1frame%d.jpg" % frame_count, fgmask)
            cv2.imshow('frame',frame)
            cv2.imshow('frame1',frame1)
            frame_count += 1
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break
            
            fps =  np.float16((1 / (time.time() - start)))   
             
        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise

cv2.destroyAllWindows()
cap.release()