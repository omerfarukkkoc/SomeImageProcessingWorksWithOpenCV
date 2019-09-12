# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 18:50:43 2017

@author: omerf
"""

import cv2
import numpy as np
import sys
import time
from datetime import datetime

fps = 0

# cap = cv2.VideoCapture('sampleVideos/markorvideo2.mp4')

cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)
print(cap.get(5))

if cap.isOpened()==True: 
    print ('Kamera Açıldı')
        
else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)

frame_count = 0

while(1):
        
        try:
            start = int(round(time.time()*1000))
            s = datetime.now()
            ret, frame = cap.read()
    
            if ret != True:
                print ('HATA!! Frame Alınamıyor \nYeniden Başlatın')
                cv2.destroyAllWindows()
                cap.release()
                break
                exit(1)
                
            cv2.putText(frame, "Fps: "+str(fps), (5,15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)


            e = datetime.now()
            cv2.putText(frame, "e: " + str(e - s), (5, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
            end = time.time() - start


            cv2.imshow('frame',frame)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                print("Çıkış Yapıldı")
                break

            fps = np.float16((1 / (time.time() - start)))
            # print("fps:" + str(fps) + " datetime:" + str(e-s) + " end:" + str(end))
            # cv2.imwrite("aa", frame)

            end = int(round(time.time()*1000))
            cv2.imwrite('25temmuzimgs/' + str(end) + "-" + str(end-start) + '.jpg', frame)

        except:
            print("Beklenmedik Hata!!! ", sys.exc_info()[0])
            raise

cv2.destroyAllWindows()
cap.release()