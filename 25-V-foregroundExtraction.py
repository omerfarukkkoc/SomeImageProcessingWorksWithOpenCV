# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 14:46:40 2017

@author: omerf
"""
import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)

if cap.isOpened()==True: 
    print ('Kamera Açıldı')
        
else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)


while(1):
        
        try:
            ret, frame = cap.read()
    
            if ret != True:
                print ('HATA!! Frame Alınamıyor \nYeniden Başlatın')
                cv2.destroyAllWindows()
                cap.release()
                break
                exit(1)
            
            original = frame
            
            frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
            
            
            mask = np.zeros(frame.shape[:2],np.uint8)

            bgdModel = np.zeros((1,65),np.float64)
            fgdModel = np.zeros((1,65),np.float64)
            
            rect =(100,75,200,200)
            cv2.grabCut(frame,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
            mask2 = np.where((mask==2)|(mask==0),1,0).astype('uint8')
            frame = frame*mask2[:,:,np.newaxis]
            
            cv2.imshow('original',original)
            cv2.imshow('frame',frame)
            
            
            
            
            
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break
            
        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise

cv2.destroyAllWindows()
cap.release()