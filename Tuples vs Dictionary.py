# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:42:04 2026

@author: aarus
"""

def robot_info():
    return"Robo", 100, "Ready"
    
name, battery, status = robot_info()

# Info
print("Name:",name)
print("Battery:",battery)
print("Status:",status)

# Dictionary vs Tuple

# brackets = {}, ()
# stores = key-value, values
# accessing = key/name, Position/Index
# changeable = yes, No
# example = {"age": 14}, (10,20,30)

student = {"name": "Aarush",
           "age": 13,
           "country": "India"}

print(student["name"])
