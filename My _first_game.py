# -*- coding: utf-8 -*-
"""
Created on Sun May 17 20:02:01 2026

@author: aarush
"""

import pygame

#start pygame
pygame.init()

#create game window 
screen = pygame.display.set_mode((800,600))

# Window title
pygame.display.set_caption("My First game")

# Game loop variable

running = True

# Main game loop

while running:

    # Check events
    for event in pygame.event.get():

        # Close window
        if event.type == pygame.QUIT:
            running = False

        # Fill background color
        screen.fill((0, 0, 0))

        # Draw rectangle
        pygame.draw.rect(
            screen, (0, 255, 0),
           (300, 200, 200, 100))
        #update display
        pygame.display.update()
        
pygame.quit()