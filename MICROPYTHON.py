#!/usr/bin/env python
# coding: utf-8

# # Rasberry PI
# 

# In[2]:


import machine      # brings in the tools to talk to hardware
import time         # brings in the clock/watch

led = machine.Pin("LED", machine.Pin.OUT)  # tells Pico that LED is an output light

while True:         # do this forever
    led.on()        # turn the light on
    time.sleep(0.5) # wait half a second
    led.off()       # turn the light off
    time.sleep(0.5) # wait again


# # Simulating LED Class not real

# In[7]:


class FakeLED 
    def on(self): print("LED on")
    def off(self): print("LED on")
        
led = FakeLED()

for i in range(3):
    led.on()
    print("waiting...")
    led.off()
    print("waiting...")


# # Light Sensor

# In[8]:


light_value = 50-100

if light_value < 50:
    print("It is dark! Turn on light!")
    
else:
    print("It is bright! Turn off the light!")


# # Ultrasonic Sensor 

# In[16]:


distance_centimeter = 60

if distance_centimeter < 50:
    print("Stop! Obstacle ahead!")
    
else: 
    print("Path is clear! Move on!")


# # PIR motion sensor

# In[23]:


motion_detected = True

if motion_detected:
    print("Motion detected! Lock the place and alert Police!")

else:
    print("Place is safe! Chill!")


# In[ ]:





# In[24]:


light = 20
distance = 10
motion = True 

if light < 50 and distance < 15 and motion:
    print("Alert! Danger close to you! ")
    
else:
    print("You are safe buddy!")


# In[ ]:




