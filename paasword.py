# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 10:45:30 2026

@author: aarus
"""

def login_system(password, max_attempts=3):
    attempts = max_attempts
    
    while attempts > 0:
        user_input = input("Enter password:")
        
        if user_input == password:
            return "Access granted"
        
        attempts -= 1
    return"System locked"
   
print(login_system("python"))

