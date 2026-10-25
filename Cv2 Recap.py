# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:55:31 2026

@author: aarus
"""

import cv2 

# Open default camera
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Could not access camera")
        break
    
    # show camera feed 
    
    cv2.imshow("Camera",frame)
    
    #press q to quit
    if cv2.waitKey(5) & 0xFF == ord('q'):
       break 
   

#clean up
cap.release()
cv2.destroyAllWindows()
   