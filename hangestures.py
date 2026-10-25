# -- coding: utf-8 --
"""
Created on Sun Jun  7 11:15:03 2026

@author: Saikumar.Gudavadla
"""

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)

hands = mp.solutions.hands.Hands()
draw = mp.solutions.drawing_utils

while True:
    ret, frame = cap.read()

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    text = "No Hand"

    if result.multi_hand_landmarks:
        for hand in result.multi_hand_landmarks:

            thumb_tip = hand.landmark[4]
            thumb_joint = hand.landmark[3]

            # Simple thumbs up rule
            if thumb_tip.y < thumb_joint.y:
                text = "👍 Like"
            else:
                text = "👎 Dislike"

            draw.draw_landmarks(
                frame,
                hand,
                mp.solutions.hands.HAND_CONNECTIONS
            )

    cv2.putText(
        frame,
        text,
        (20, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    cv2.imshow("Sign Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()