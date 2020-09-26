# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 12:35:59 2020

@author: khan
"""

import cv2 as cv

list_contours = []

# Reading image from directory
img = cv.imread('test.jpg')#,0)
imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# The function applies fixed-level thresholding to a multiple-channel array. 
# The function is typically used to get a bi-level (binary) image out of a grayscale image 
# ( compare could be also used for this purpose) or for removing a noise, that is, filtering out 
# pixels with too small or too large values.

ret,thresh = cv.threshold(imgray,230,255,0)
cv.imshow('Threshold_image', thresh)
cv.waitKey(0)
img2, contours, hierarchy = cv.findContours(thresh, 1, 2)

for i in range(0,len(contours)):
    cnt = contours[i]
    # Image moments help you to calculate some features like center of mass of the object, area of the object etc.
    M = cv.moments(cnt)
    if(M['m00'] != 0):
        # Centroid
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        # Contour area is given by the function cv.contourArea() or from moments, M['m00']
        area = cv.contourArea(cnt)
        # It is also called arc length. It can be found out using cv.arcLength() function. 
        # Second argument specify whether shape is a closed contour (if passed True), or just a curve.
        perimeter = cv.arcLength(cnt,True)
        epsilon = 0.1*cv.arcLength(cnt,True)
        approx = cv.approxPolyDP(cnt,epsilon,True)
        if(area > 6400 and area < 380000):
            list_contours.append(cnt)
        
test = cv.drawContours(img, list_contours, -1, (0,255,0), 5)

cv.imshow('Output_image', test)

cv.waitKey(0)
cv.destroyAllWindows()