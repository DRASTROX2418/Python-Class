# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 16:09:33 2026

@author: aarus
"""

# OpenCV 
# It can draw coordinates on top of a video feed.

#OpenCV as [Read->modify_>show]

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error:could not find your camera")
else:
    print("success! Your camera is working")

#Take photo and then show it
ret, frame = cap.read()
cv2.imshow("Test Photo",frame)
    
#wait for you to press a key , then close
cv2.waitKey(0)
cv2.destroyAllwindows()
cap.release()