# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 15:26:47 2017

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

face_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascades/haarcascade_eye.xml')

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
            
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)
            
            for (x,y,w,h) in faces:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = frame[y:y+h, x:x+w]
                
                eyes = eye_cascade.detectMultiScale(roi_gray, 1.2, 5)
                
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                    
        
        
            cv2.putText(frame, "Fps: "+str(fps), (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

            cv2.imshow('frame',frame)
            
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