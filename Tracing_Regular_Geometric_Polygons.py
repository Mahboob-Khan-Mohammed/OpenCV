# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 12:21:10 2020

@author: khan
"""


import cv2
import numpy as np
import time

def Polygon_side(angle):
    (x, y) = (int(256 + 150*np.cos(angle*np.pi/180)), int(256 + 150*np.sin(angle*np.pi/180)))
    return (x,y)

# black blank image
blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
#Syntax: cv2.circle(image, center_coordinates, radius, color, thickness)
angle = 0
# Change Polygon_angle for different shapes
polygon_angle = 270
(x1, y1) = Polygon_side(polygon_angle)

while(True):
    (x2,y2) = Polygon_side(angle)
    image = cv2.line(blank_image,(x1,y1),(x2,y2),(255,255,255),5)
    cv2.imshow("Test Image", image)
    (x1, y1) = (x2, y2)
    angle += polygon_angle
    time.sleep(0.5)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
   
cv2.destroyAllWindows()