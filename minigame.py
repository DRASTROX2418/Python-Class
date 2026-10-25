# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:42:38 2026

@author: aarus
"""

import pygame
pygame.init()

#create game window 
screen = pygame.display.set_mode((800,600))

x = 30

running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill screen with black
    screen.fill((0, 0, 0))

    # Move right
    x += 0.0001

    # Draw rectangle
    pygame.draw.rect(screen, (0, 255, 0), (x, 250, 100, 100))

    # Update display
    pygame.display.update()
    
pygame.quit()
