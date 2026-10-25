#!/usr/bin/env python
# coding: utf-8

# # Robo Arm Project

# In[1]:


import pygame
pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

# Make a simple arm rectangle
arm = pygame.Surface((100, 10))  # width, height
arm.fill((0, 128, 255))
arm_orig = arm.copy()

angle = 0  # Start at 0 degrees

while True:
    screen.fill((255, 255, 255))

    # Rotate arm by angle
    rotated = pygame.transform.rotate(arm_orig, -angle)
    rect = rotated.get_rect(center=(200, 200))  # pivot from center

    screen.blit(rotated, rect.topleft)
    pygame.display.flip()

    angle += 1
    if angle > 180: angle = 0

    clock.tick(30)  # Limit to 30 FPS


# In[2]:


pip install pygame


# # Definitions
# 

# In[1]:


# Motor
A Motor is alittle machine that spins when you give it electricity.
Turn wheels and fans or solar panels
# Servo Motor
A Servo motor turns to a specific angle like 0° 90° or 180°.
It is a smart motion
# Solar Panel
A solar panel is a magic sheet which turndsunlight to electricity.
You can use to power things which use energy
# Sensor
Tiny Gagdget that can feel light,temperature and motion


# In[5]:


import ipywidgets as widgets 
from IPython.display import display
import time


# In[4]:


pip install ipywidgets


# In[ ]:


left_light = widgets.IntSlider(description='Left light', min = 0, max = 100, value = 50)
right_light = widgets.Intslider(description = 'Right light', min = 0, max =100, value = 50)
display(left_light, right_light)
 
    
def track_sun():
    if left_light.value > right_light.value:
        print("Turning Solar Panel to the left")
    elif right_light.value > left_light.value:
        print("Turning Solar Panel to the right")
    else:
        print("Panel is centered")
        
        
button = widgets.Button(description ="Track Sun")
def on_button_click(b):
    track_sun()
    
button.on

