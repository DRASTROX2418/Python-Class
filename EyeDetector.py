# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:16:33 2026

@author: aarus
"""

import cv2

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.3,3)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),3)
        roi_gray = gray[y:y+h, x:x+w]
        roi_colour = frame[y:y+h, x:x+w]
        
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes :
            cv2.rectangle(roi_colour,
                          (ex,ey),
                          (ex+ew, ey+eh),
                          (255,0,0),2)
            
            cv2.imshow("Face+Eye Detection", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
               break 
           
cap.release()
cv2.destroyAllWindows()
        

        
        