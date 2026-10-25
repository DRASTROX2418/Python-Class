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
from PIL import Image
# open the image file
img = Image.open("aarush.jpg")

#image width and height
width, height = img.size

for x in range (width):
    for y in range(height):
        
        #get the current pixel's Red, green and blue values
        r,g,b = img.getpixel((x,y))
        
        #Example:Darkmode (lowers brightness by 50%)
        r = int(r*1.5)
        g = int(g*2.5)
        b = int(b*3.5)

        #put the new, modififed pixel back in to the image
        img.putpixel((x,y),(r,g,b))

#show the final edited image on the screen
img.show()




       