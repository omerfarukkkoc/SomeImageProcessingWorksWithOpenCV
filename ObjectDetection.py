"""
Created on Sat Mar 10 19:54:38 2018

@author: omerfarukkoc
"""

import cv2
import numpy as np
import sys
from time import sleep
import pan_tilt_servo_write


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

# # # # # # variables # # # # # #
hueMin = 0
saturationMin = 0
valueMin = 0
ResizeWidth = 1024
ResizeHeight = 768
LocationSensitivity = 5
# # # # # # variables # # # # # #

hueMax = 179
saturationMax = 255
valueMax = 255

cv2.namedWindow('Renk Ayar Penceresi')
cv2.createTrackbar('H-Min', 'Renk Ayar Penceresi', 0, 179, nothing)
cv2.createTrackbar('S-Min', 'Renk Ayar Penceresi', 0, 255, nothing)
cv2.createTrackbar('V-Min', 'Renk Ayar Penceresi', 0, 255, nothing)

cv2.setTrackbarPos('H-Min', 'Renk Ayar Penceresi', hueMin)
cv2.setTrackbarPos('S-Min', 'Renk Ayar Penceresi', saturationMin)
cv2.setTrackbarPos('V-Min', 'Renk Ayar Penceresi', valueMin)

ColorOptionFrame = np.zeros((1, 350, 3), np.uint8)

erodeMatrix = np.ones((3, 3), np.uint8)
dilateMatrix = np.ones((8, 8), np.uint8)

Cam = cv2.VideoCapture(0)

width = Cam.get(3)
height = Cam.get(4)
fps = Cam.get(5)

PointControl = False
Count = 0


if Cam.isOpened() == True:
    print('\nKamera Açıldı')
    print("Width: ", width, "\nHeight: ", height, "\nFPS: ", fps)

else:
    print('HATA!! \nKamera Açılamadı!!')
    exit(1)

XString = "-"
YString = "-"

while (1):

    try:
        cv2.imshow('Renk Ayar Penceresi', ColorOptionFrame)
        ret, frame = Cam.read()

        if ret != True:
            print('HATA!! Kameradan Frame Alınamıyor \nYeniden Başlatın')
            cv2.destroyAllWindows()
            Cam.release()
            break
            exit(1)

        hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        hueMin = cv2.getTrackbarPos('H-Min', 'Renk Ayar Penceresi')
        saturationMin = cv2.getTrackbarPos('S-Min', 'Renk Ayar Penceresi')
        valueMin = cv2.getTrackbarPos('V-Min', 'Renk Ayar Penceresi')

        lowerLimit = np.array([hueMin, saturationMin, valueMin], dtype=np.uint8)
        upperLimit = np.array([hueMax, saturationMax, valueMax], dtype=np.uint8)

        threshold = cv2.inRange(hsvFrame, lowerLimit, upperLimit)
        threshold = cv2.erode(threshold, erodeMatrix)
        threshold = cv2.dilate(threshold, dilateMatrix)

        locations, area = findContour(threshold)
        x, y, width, height = locations
        object_center_x = x + (width // 2)
        object_center_y = y + (height // 2)
        Points = object_center_x, object_center_y

        if area > 1000:
            cv2.rectangle(frame, (x, y), (x + width, y + height), (255, 0, 0), 2)
            cv2.circle(frame, (object_center_x, object_center_y), 5, (255, 255, 0), 3)

            Count += 1
            if (Count % 5) == 0:
                OldPoints = Points
                PointControl = True

            if PointControl:
                if (Points[0] - OldPoints[0]) > LocationSensitivity:
                    XString = "Sag"
                    pan_tilt_servo_write.pan_positive()
                elif (OldPoints[0] - Points[0]) > LocationSensitivity:
                    XString = "Sol"
                    pan_tilt_servo_write.pan_negative()
                else:
                    XString = "-"

                if (Points[1] - OldPoints[1]) > LocationSensitivity:
                    YString = "Asagi"
                    pan_tilt_servo_write.tilt_positive()
                elif (OldPoints[1] - Points[1]) > LocationSensitivity:
                    YString = "Yukari"
                    pan_tilt_servo_write.tilt_negative()
                else:
                    YString = "-"

                cv2.putText(frame, "X Hareket: "+str(XString), (5, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1,
                            cv2.LINE_AA)
                cv2.putText(frame, "Y Hareket: "+str(YString), (5, 35), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1,
                            cv2.LINE_AA)


        frame = cv2.resize(frame, (ResizeWidth, ResizeHeight), interpolation=cv2.INTER_LINEAR)
        cv2.imshow('Frame', frame)
        # cv2.imshow("Threshold", threshold)

        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            print("Çıkış Yapıldı")
            break

    except:
        print("Beklenmedik Hata!!! ", sys.exc_info()[0])
        raise

cv2.destroyAllWindows()
Cam.release()
