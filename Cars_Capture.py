# -*- coding: utf-8 -*-
"""
Created on Sun May 10 19:18:18 2026

@author: aarus
"""
import cv2 
#Loading Car detector

car_cascade = cv2.CascadeClassifier('cars.xml')

#Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Failed to grab frame")
        break

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    #Detect Cars
    
    cars = car_cascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors = 3)
    
    #Draw Boxes 
    
    
    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,"car",(x,y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,(255,0,0),2)
        
        cv2.imshow("Face Detection", frame)

        if cv2.waitKey(5) & 0xFF == ord('q'):
           break 
       
        cap.release()
        cv2.destroyAllWindows()
        