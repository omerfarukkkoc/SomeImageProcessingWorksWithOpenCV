# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 18:28:21 2017

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
            
            frame = cv2.resize(frame, (400, 300), interpolation = cv2.INTER_LINEAR) 
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            cv2.rectangle(frame, (199,149), (201,151), (255,0,0), 2)
            
            color = frame[200, 150]
            
            B = color[0]
            G = color[1]
            R = color[2]
            
            print ('B,G,R')
            print (B,G,R)
        
            
            V = max(B,G,R)
            S = round( ( ( V - min(B,G,R) ) / V ) * 255 )
            H = round( ( ( 240 + 60*(R - G) ) / ( V - min(B,G,R) ) ) /2 )
            
            H = H.astype(np.uint8)
            S = S.astype(np.uint8)
            V = V.astype(np.uint8)
            
            
            print ('H,S,V')
            print (H,S,V)
        
            lower = np.array([H, S, V])
            #lower = np.array([251,219,7])
            
            print ('lower')
            print (lower)
            
            upper = np.array([179, 255, 255])
            
            #lower = np.array([110, 50, 50])
            #upper = np.array([130, 255, 255])
            
            #mask = cv2.inRange(hsv, lower, upper)
            #mask = cv2.convertScaleAbs(mask)
            res = cv2.bitwise_and(frame,frame, mask= mask)
            
            cv2.imshow('frame',frame)
            #cv2.imshow('hsv',hsv)
            #cv2.imshow('mask',mask)
            #cv2.imshow('res',res)
            
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break
                
            
            
        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise

      
cv2.destroyAllWindows()
cap.release()

