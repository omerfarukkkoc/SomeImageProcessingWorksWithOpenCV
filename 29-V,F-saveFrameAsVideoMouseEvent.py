# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 17:00:05 2017

@author: omerf
"""

import cv2
import sys
import time
import numpy as np

count = 0
ix = iy = -1
fps = 0

def takePhoto(event, x, y, flags, param):
    global count
    
    global ix,iy
    
    
    if event == cv2.EVENT_LBUTTONDBLCLK:
        
        cv2.imwrite("sampleImages/frame%d.jpg" % count, frame)
        
        print ('frame%d.jpg kaydedildi' % count)
        
        count = count+1
        

    
    elif event == cv2.EVENT_MOUSEMOVE:
        ix,iy = x,y
    
    #elif event == cv2.EVENT_LBUTTONUP:
      



cap = cv2.VideoCapture(0)

cv2.namedWindow('frame')
cv2.setMouseCallback("frame",takePhoto)

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
            cv2.putText(frame, "x: "+str(ix)+" , "+"y: "+str(iy), (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.putText(frame, "Frame Almak icin Cift Tikla", (5,290), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            cv2.putText(frame, "Fps: "+str(fps), (5,35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            
            
            
            cv2.imshow('frame', frame)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break
                
            
            fps =  np.float16((1 / (time.time() - start)))
        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise
            

    


cap.release()      
cv2.destroyAllWindows()