# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 10:27:24 2026

@author: aarus
"""

import tkinter as tk
import random
import winsound

score = 0
attempts = 0 
max_attempts = 5
player = "Cristiano Ronaldo"
team = "Portugal"

goalkeeper = "Emiliano Martinez"
opponent = "Argentina"

window = tk.Tk()
window.title("Football Penalty Shootout")
window.geometry("800x600")

canvas = tk.Canvas(window, width=700, height=400, bg="green")
canvas.pack(pady=10
# Field
canvas.create_rectangle(250, 40, 450, 100, width=4)   # Goal
canvas.create_line(0, 350, 700, 350, width=3)         # Penalty line

# Goalkeeper
keeper = canvas.create_oval(330, 60, 370, 100, fill="blue")

# Ball
ball = canvas.create_oval(335, 320, 365, 350, fill="white")

score_label = tk.Label(window, text="Goals: 0", font=("Arial", 16))
score_label.pack()

attempts_label = tk.Label(
    window, text= "Attempts:0/5", font=("Arial",16))
attempts_label.pack()

result = tk.Label(window, text="Choose a direction", font=("Arial", 16))
result.pack()

def shoot(direction):
    global score, attempts
    
    if attempts >= max_attempts:
        result.config(text="Game Over!")
        return

    # Reset ball position
    canvas.coords(ball, 335, 320, 365, 350)

    keeper_side = random.choice(["Left", "Center", "Right"])

    if keeper_side == "Left":
        canvas.coords(keeper, 270, 60, 310, 100)

    elif keeper_side == "Center":
        canvas.coords(keeper, 330, 60, 370, 100)

    else:
        canvas.coords(keeper, 390, 60, 430, 100)

    # Ball target
    if direction == "Left":
        target_x = 280
    elif direction == "Center":
        target_x = 350
    else:
        target_x = 420

    # Animate ball
    for i in range(20):
        canvas.move(ball, (target_x-350)/20, -12)
        window.update()
        window.after(20)
        
    attempts +=1
    attempts_label.config(
        text=f"Attempts: {attempts}/{max_attempts}")
    

    if direction == keeper_side:
        winsound.Beep(500, 300)
        result.config(
            text=f"{goalkeeper} SAVED {player}'s shot!")
        
    else:
        winsound.Beep(1000, 500)
        score += 1
        score_label.config(text=f"Goals: {score}")
        result.config(text=f"GOAL! {player} scores for {team}!")
        
    if attempts == max_attempts:
        result.config(
            text=f" Match Finished with FULL TIME! {player} scored {score}/{max_attempts}")

button_frame = tk.Frame(window)
button_frame.pack(pady=10)

tk.Button(button_frame, text="Left",
          command=lambda: shoot("Left")).grid(row=0, column=0, padx=10)

tk.Button(button_frame, text=" Center",
          command=lambda: shoot("Center")).grid(row=0, column=1, padx=10)

tk.Button(button_frame, text="Right",
          command=lambda: shoot("Right")).grid(row=0, column=2, padx=10)

window.mainloop()