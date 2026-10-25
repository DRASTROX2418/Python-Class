# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 09:13:57 2026

@author: aarus
"""

# Pixel 
# Every image is made of thousands of tiny squares called pixels. 
# Each pixel  has 3 values 

# pixel = (R,G,B)

# red = (255,0,0)
# black = (0,0,0)
# white = (255,255,255)
# bigger number = brighter colours

# PIL = Python Imaging Library 
from PIL import image 
# open image file
img = image.open("JE-U15.jpeg")

# image width and height 

width,height = img.size

for x in range (width):
    for y in range (height):

       # get current rgb pixel values
        r,g,b = img.getpixel((x,y))
        
       # Darkmode(Lower brightness by 50%)
        r = int(r*0.5)
        g = int(g*0.5)
        b = int(b*0.5)
           
       #put new pixels into image
        img.putpixel((x,y)),((r,g,b))
       
       
# show edited image 
img.show()










       