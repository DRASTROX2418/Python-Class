# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:14:24 2026

@author: aarus
"""

import cv2

#Load cascades
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml')

#Load sunglasses image

sunglasses = cv2.imread("sunglasses.png",cv2.IMREAD_UNCHANGED)

#Open camera

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()
    
    if not ret:
        break
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.3,3)
    
    for (x,y,w,h) in faces:
        
        #Draw face rectangle
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0),2)
        
        #Resize sunglasses
        glass_width = w 
        glass_height = int(h/3)
        
        resized_glass = cv2.resize(
            sunglasses,
            (glass_width, glass_height)
        )
        
        
        #Position sunglasses
        y1 = y+h // 4
        y2 = y1 + glass_height
        
        x1 = x
        x2 = x1 + glass_width
        
        #prevent out of bounds
        if y2 > frame.shape[0] or x2 > frame.shape[1]:
           continue
    
        #overlay sunglasses
        frame[y1:y2, x1:x2] = resized_glass[:, :, :3]
    
        cv2.imshow("Cool AI Filter", frame)
   
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break 
           
cap.release()
cv2.destroyAllWindows()
        
        

