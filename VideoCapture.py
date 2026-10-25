# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:23:35 2026

@author: aarus
"""

#face_cascade = cv2.CascadeClassifier

import cv2
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break
    # Convert to grayscale
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray,1.1,5)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0),2)
        
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(5) & 0xFF == ord('q'):
       break 
   
    cap.release()
    cv2.destroyAllWindows()