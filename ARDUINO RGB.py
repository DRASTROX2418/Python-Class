#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -- coding: utf-8 --
"""
Created on Sun Dec  7 10:09:37 2025

@author: Saikumar.Gudavadla
"""

import tkinter as tk
import serial
import time

# ----------------------------------------------------
# Change this to your Arduino COM port:
# Windows example: "COM3"
# Mac/Linux: "/dev/ttyUSB0"
# ----------------------------------------------------
PORT = "COM3"
BAUD = 9600

# connect to Arduino
ser = serial.Serial(PORT, BAUD)
time.sleep(2)  # wait for Arduino to reboot

# GUI setup
root = tk.Tk()
root.title("Arduino LED Visualizer")

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 250

canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="black")
canvas.pack()

# Bar width and spacing
bar_width = 80

# Create bars (height starts at zero)
red_bar = canvas.create_rectangle(40, CANVAS_HEIGHT, 40 + bar_width, CANVAS_HEIGHT, fill="red")
green_bar = canvas.create_rectangle(160, CANVAS_HEIGHT, 160 + bar_width, CANVAS_HEIGHT, fill="green")
blue_bar = canvas.create_rectangle(280, CANVAS_HEIGHT, 280 + bar_width, CANVAS_HEIGHT, fill="blue")

label = tk.Label(root, text="Waiting for Arduino...", fg="white", bg="black")
label.pack(pady=5)


def update_gui():
    """
    Reads a line from Arduino in the format: 1,0,1
    And updates the GUI bar heights.
    """
    try:
        line = ser.readline().decode().strip()
        parts = line.split(",")

        # ONLY ENTER HERE IF 3 VALUES RECEIVED
        if len(parts) == 3:
            r = int(parts[0])
            g = int(parts[1])
            b = int(parts[2])

            label.config(text=f"LED States → R:{r}, G:{g},B:{b}")

            # Convert LED ON/OFF to bar heights
            def bar_height(val):
                return CANVAS_HEIGHT - (val * 200)

            canvas.coords(red_bar, 40, bar_height(r), 40 + bar_width, CANVAS_HEIGHT)
            canvas.coords(green_bar, 160, bar_height(g), 160 + bar_width, CANVAS_HEIGHT)
            canvas.coords(blue_bar, 280, bar_height(b), 280 + bar_width, CANVAS_HEIGHT)

    except Exception as e:
        print("Read error:", e)

    root.after(50, update_gui)


# Start updating GUI
update_gui()

# Start GUI loop
root.mainloop()


# In[4]:


# -- coding: utf-8 --
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# -------------------------
# Data + helper functions
# -------------------------

SUBJECTS = ["Codelingual", "Table Tennis", "Badminton"]  # list (datatype)

def safe_int(text: str) -> int:
    """Convert input string to int (0..100) or raise ValueError."""
    value = int(text)
    if not (0 <= value <= 100):
        raise ValueError("Score must be 0..100")
    return value

def collect_scores(entries: dict) -> dict:
    """
    Read scores from entry widgets.
    Returns:
        scores = {
          "Liam": {"Codelingual": 90},
          ...
        }
    """
    scores = {}  # dict (datatype)
    for student_name, subj_entries in entries.items():
        scores[student_name] = {}
        for subject, entry in subj_entries.items():
            scores[student_name][subject] = safe_int(entry.get())
    return scores

def show_donut_plots(scores: dict) -> None:
    """Plot one donut chart per student."""
    students = list(scores.keys())

    fig, axes = plt.subplots(1, 3, figsize=(10, 4))
    fig.suptitle("Donut Charts: Scores by Subject", fontsize=14)

    for ax, student in zip(axes, students):
        values = [scores[student][s] for s in SUBJECTS]
        wedges, _ = ax.pie(values, labels=SUBJECTS, startangle=90)
        # donut hole
        centre_circle = plt.Circle((0, 0), 0.55, fc="white")
        ax.add_artist(centre_circle)
        ax.set_title(student)
        ax.axis("equal")

    plt.tight_layout()
    plt.show()

# -------------------------
# GUI
# -------------------------

def on_plot():
    """Button callback: read data, validate, plot donuts."""
    try:
        scores = collect_scores(entry_map)
        show_donut_plots(scores)
    except ValueError as e:
        messagebox.showerror("Invalid Input", str(e))

root = tk.Tk()
root.title("3 Students Score Donut Plot")

tk.Label(root, text="Enter scores (0 to 100) for each student:", font=("Arial", 11, "bold")).grid(
    row=0, column=0, columnspan=4, padx=8, pady=8, sticky="w"
)

# entry_map is a nested dict: {student: {subject: Entry}}
entry_map = {}

students = ["Liam   ", "Arnav", "Aarush"]

# Header row
tk.Label(root, text="Student").grid(row=1, column=0, padx=6, pady=4)
for j, subject in enumerate(SUBJECTS, start=1):
    tk.Label(root, text=subject).grid(row=1, column=j, padx=6, pady=4)

# Input rows
for i, student in enumerate(students, start=2):
    tk.Label(root, text=student).grid(row=i, column=0, padx=6, pady=4, sticky="w")
    entry_map[student] = {}
    for j, subject in enumerate(SUBJECTS, start=1):
        e = tk.Entry(root, width=8)
        e.insert(0, "0")  # default value
        e.grid(row=i, column=j, padx=6, pady=4)
        entry_map[student][subject] = e

# Button
tk.Button(root, text="Plot Donut Charts", command=on_plot, width=20).grid(
    row=6, column=0, columnspan=4, padx=8, pady=10
)

root.mainloop()


# In[ ]:




