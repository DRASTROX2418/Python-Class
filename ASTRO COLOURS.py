#!/usr/bin/env python
# coding: utf-8

# # 27.12.2024

# #include <Adafruit_NeoPixel.h>
# 
# #define PIN 6           // Pin connected to the LED data pin
# #define NUMPIXELS 1     // Number of LEDs (adjust if using more)
# Adafruit_NeoPixel pixels(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);
# 
# void setup() {
#   Serial.begin(9600);
#   pixels.begin();  // Initialize the LED strip
# }
# 
# void loop() {
#   if (Serial.available() > 0) {
#     // Read incoming color values
#     String data = Serial.readStringUntil('\n');
#     int comma1 = data.indexOf(',');
#     int comma2 = data.lastIndexOf(',');
# 
#     if (comma1 > 0 && comma2 > comma1) {
#       int red = data.substring(0, comma1).toInt();
#       int green = data.substring(comma1 + 1, comma2).toInt();
#       int blue = data.substring(comma2 + 1).toInt();
# 
#       // Set the LED color
#       pixels.setPixelColor(0, pixels.Color(red, green, blue));
#       pixels.show();
#     }
#   }
# }
# 
# 

# In[ ]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "serial-arduino",
   "metadata": {},
   "outputs": [],
   "source": [
    "import serial\n",
    "import time\n",
    "\n",
    "# Connect to Arduino (replace 'COM3' with your Arduino's port and match the baud rate)\n",
    "arduino_port = \"COM3\"  # Adjust for your system\n",
    "baud_rate = 9600\n",
    "ser = serial.Serial(arduino_port, baud_rate, timeout=1)\n",
    "time.sleep(2)  # Wait for Arduino to initialize\n",
    "\n",
    "def send_color(red, green, blue):\n",
    "    \"\"\"\n",
    "    Send RGB color values to Arduino.\n",
    "    :param red: Intensity of red (0-255)\n",
    "    :param green: Intensity of green (0-255)\n",
    "    :param blue: Intensity of blue (0-255)\n",
    "    \"\"\"\n",
    "    color_data = f\"{red},{green},{blue}\\n\"\n",
    "    ser.write(color_data.encode())\n",
    "    print(f\"Sent: {color_data.strip()}\")\n",
    "\n",
    "def rainbow_effect():\n",
    "    \"\"\"\n",
    "    Loop through a rainbow color sequence.\n",
    "    \"\"\"\n",
    "    for r in range(0, 256, 10):  # Fade red up\n",
    "        send_color(r, 0, 255 - r)\n",
    "        time.sleep(0.05)\n",
    "    for g in range(0, 256, 10):  # Fade green up\n",
    "        send_color(255 - g, g, 0)\n",
    "        time.sleep(0.05)\n",
    "    for b in range(0, 256, 10):  # Fade blue up\n",
    "        send_color(0, 255 - b, b)\n",
    "        time.sleep(0.05)\n",
    "\n",
    "# Example usage\n",
    "rainbow_effect()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

