# -*- coding: utf-8 -*-
"""
Created on Sat Mar 10 19:54:38 2018

@author: omerfarukkoc
"""

import cv2
import numpy as np
import sys


def findContour(frame):
    areas = 0
    contourIndex = 0
    #image, contours, hierarchy = cv2.findContours(frame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    image, contours, hierarchy = cv2.findContours(frame, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for idx, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if (area > areas):
            areas = area
            contourIndex = idx

    locationss = (0, 0, 2, 2)
    if len(contours) > 0:
        locationss = cv2.boundingRect(contours[contourIndex])

    return locationss, areas

def nothing(x):
    pass


hueMin = 0
hueMax = 179

saturationMin = 0
saturationMax = 255

valueMin = 0
valueMax = 255

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

img = np.zeros((1, 350, 3), np.uint8)

erodeMatrix  = np.ones((3, 3), np.uint8)
dilateMatrix = np.ones((8, 8), np.uint8)

cap = cv2.VideoCapture(0)
if cap.isOpened() == True:
    print('Kamera Açıldı')

else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)


while (True):

    try:
        cv2.imshow('Renk Ayar Penceresi', img)
        ret, frame = cap.read()

        if ret != True:
            print('HATA!! Frame Alınamıyor \nYeniden Başlatın')
            cv2.destroyAllWindows()
            cap.release()
            break
            exit(1)

        frame = cv2.resize(frame, (640, 480), interpolation=cv2.INTER_LINEAR)
        reverseFrame = 255 - frame

        hsvFrame = cv2.cvtColor(reverseFrame, cv2.COLOR_BGR2HSV)

        hueMin = cv2.getTrackbarPos('H-Min', 'Renk Ayar Penceresi')
        saturationMin = cv2.getTrackbarPos('S-Min', 'Renk Ayar Penceresi')
        valueMin = cv2.getTrackbarPos('V-Min', 'Renk Ayar Penceresi')
        hueMax = cv2.getTrackbarPos('H-Max', 'Renk Ayar Penceresi')
        saturationMax = cv2.getTrackbarPos('S-Max', 'Renk Ayar Penceresi')
        valueMax = cv2.getTrackbarPos('V-Max', 'Renk Ayar Penceresi')

        lowerLimit = np.array([hueMin, saturationMin, valueMin], dtype=np.uint8)
        #lowerLimit = np.array([100, 85, 155], dtype=np.uint8)
        upperLimit = np.array([hueMax, saturationMax, valueMax], dtype=np.uint8)

        threshold = cv2.inRange(hsvFrame, lowerLimit, upperLimit)
        threshold = cv2.erode(threshold, erodeMatrix)
        threshold = cv2.dilate(threshold, dilateMatrix)

        locations, area = findContour(threshold)
        x, y, width, height = locations

        if (width * height) > 10:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)


        cv2.imshow('Frame', frame)
        cv2.imshow("Threshold", threshold)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("Çıkış Yapıldı")
            break


    except:
        print("Beklenmedik Hata!!! ", sys.exc_info()[0])
        raise

cv2.destroyAllWindows()
cap.release()