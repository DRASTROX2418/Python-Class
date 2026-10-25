# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:10:28 2026

@author: aarus
"""

import tkinter as tk

window = tk.Tk()
window.title("AI Camera Dashboard")
window.geometry("500x300")

title = tk.Label(
    window,
    text=" AI Camera Assistant",
    font=("Arial",20)
)
title.pack(pady=10)

detected = tk.Label(
    window,
    text="Object: None",
    font=("Arial",16)
)
detected.pack()

advice = tk.Label(
    window,
    text="Waiting...",
    font=("Arial",16)
)
advice.pack()

tk.Button(window,text="Start Camera").pack(pady=20)

window.mainloop()


import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
from tensorflow.keras.models import load_model

# --------------------------------
# Load AI Model
# --------------------------------

model = load_model(
    "model/keras_model.h5",
    compile=False
)

with open("model/labels.txt", "r") as f:
    labels = [line.strip() for line in f.readlines()]

# --------------------------------
# GUI Window
# --------------------------------

window = tk.Tk()
window.title("Mouse vs Phone Detector")
window.geometry("800x700")

title = tk.Label(
    window,
    text="AI Object Detector",
    font=("Arial", 20)
)
title.pack(pady=10)

camera_label = tk.Label(window)
camera_label.pack()

detected = tk.Label(
    window,
    text="Object: None",
    font=("Arial", 16)
)
detected.pack()

confidence_label = tk.Label(
    window,
    text="Confidence: 0%",
    font=("Arial", 16)
)
confidence_label.pack()

message = tk.Label(
    window,
    text="Waiting...",
    font=("Arial", 16)
)
message.pack(pady=10)

# --------------------------------
# Camera
# --------------------------------

cap = cv2.VideoCapture(0)

# --------------------------------
# AI Camera Loop
# --------------------------------

def update_camera():

    ret, frame = cap.read()

    if ret:

        # Display camera feed
        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        image = Image.fromarray(rgb)

        image = image.resize(
            (600, 400)
        )

        photo = ImageTk.PhotoImage(image)

        camera_label.config(
            image=photo
        )

        camera_label.image = photo

        # Prepare image for model

        resized = cv2.resize(
            frame,
            (224, 224)
        )

        img = np.asarray(resized)

        img = img.astype(np.float32)

        img = (img / 127.5) - 1

        img = np.expand_dims(
            img,
            axis=0
        )

        # Predict

        prediction = model.predict(
            img,
            verbose=0
        )

        index = np.argmax(
            prediction
        )

        confidence = (
            prediction[0][index] * 100
        )

        label = labels[index]

        detected.config(
            text=f"Object: {label}"
        )

        confidence_label.config(
            text=f"Confidence: {confidence:.1f}%"
        )

        # Advice

        if "Mouse" in label:

            message.config(
                text="🖱️ Ready to Work!",
                fg="green"
            )

        elif "Phone" in label:

            message.config(
                text="Possible Distraction!",
                fg="red"
            )

        else:

            message.config(
                text="Unknown Object",
                fg="black"
            )

    window.after(
        100,
        update_camera
    )

# --------------------------------
# Start Button
# --------------------------------

def start_camera():
    update_camera()

start_btn = tk.Button(
    window,
    text="Start Camera",
    font=("Arial", 14),
    command=start_camera
)

start_btn.pack(pady=10)

window.mainloop()

cap.release()