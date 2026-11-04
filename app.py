import os
import time
import cv2
import joblib
import mediapipe as mp
import numpy as np


# Windows PowerShell ki aawaz ke liye
def speak_word(text):
  try:
    command = (
        f'powershell -Command "Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.Speak(\'{text}\')"'
    )
    os.system(command)
  except Exception as e:
    print("Speech error:", e)


# Model load karein
print("Model load ho raha hai...")
model = joblib.load("model.pkl")

# MediaPipe Both Hands Setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)
print("\n--- ISL TRANSLATOR READY ---")
print("Camera ke samne gesture karein. 'q' dabayein band karne ke liye.\n")

display_word = "Waiting for Gesture..."
last_spoken = ""
cooldown = 2.5
last_time = 0

while cap.isOpened():
  success, frame = cap.read()
  if not success:
    break

  frame = cv2.flip(frame, 1)
  h, w, c = frame.shape
  rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
  results = hands.process(rgb_frame)

  row = [0.0] * (2 * 21 * 3)
  prediction_name = ""

  if results.multi_hand_landmarks:
    for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
      if idx < 2:
        mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        start_idx = idx * 21 * 3
        for lm_idx, lm in enumerate(hand_landmarks.landmark):
          row[start_idx + (lm_idx * 3)] = lm.x
          row[start_idx + (lm_idx * 3) + 1] = lm.y
          row[start_idx + (lm_idx * 3) + 2] = lm.z

    input_data = np.array([row])
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)
    confidence = np.max(probabilities) * 100

    if confidence > 70:
      prediction_name = prediction
      display_word = prediction.upper()  # Screen par bada naam dikhane ke liye
    else:
      display_word = "Uncertain"
  else:
    display_word = "No Hand Detected"
    prediction_name = ""
    last_spoken = ""

  # --- SPEAKING LOGIC ---
  current_time = time.time()
  if prediction_name and prediction_name != "Uncertain":
    if prediction_name != last_spoken and (
        current_time - last_time > cooldown
    ):
      print(f"Speaking & Displaying: {prediction_name}")
      speak_word(prediction_name)
      last_spoken = prediction_name
      last_time = current_time

  # --- UI OVERLAY (Bada aur attractive box) ---
  # Upar ek sundar banner
  cv2.rectangle(frame, (0, 0), (w, 100), (30, 30, 30), -1)
  cv2.putText(
      frame,
      "ISL LIVE TRANSLATOR",
      (20, 30),
      cv2.FONT_HERSHEY_SIMPLEX,
      0.7,
      (200, 200, 200),
      2,
  )

  # Detect hone wala main word (Bade aksharon mein)
  cv2.putText(
      frame,
      f"Word: {display_word}",
      (20, 80),
      cv2.FONT_HERSHEY_SIMPLEX,
      1.3,
      (0, 255, 0),
      3,
  )

  cv2.imshow("ISL Translator", frame)

  if cv2.waitKey(1) & 0xFF == ord("q"):
    break

cap.release()
cv2.destroyAllWindows()