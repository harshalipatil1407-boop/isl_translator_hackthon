import csv
import cv2
import mediapipe as mp

# Saare 12 gestures ki list
gestures = [
    "hello",
    "bye",
    "good",
    "no",
    "water",
    "eat",
    "stop",
    "help",
    "pain",
    "washroom",
    "i",
    "need",
]

# MediaPipe setup for Both Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
)
mp_draw = mp.solutions.drawing_utils

print("--- ISL DATA COLLECTION (BOTH HANDS) ---")

while True:
  print("\n==============================")
  print("GESTURE MENU:")
  for idx, g in enumerate(gestures):
    print(f"{idx + 1}. {g}")
  print("0. Exit / Program Band Karein")
  print("==============================")

  try:
    choice_input = input(
        "\nKisi ek gesture ka number dalein (1-12) ya 0 dabayein: "
    ).strip()
    if not choice_input:
      continue
    choice = int(choice_input)
  except EOFError:
    print(
        "\n[Error] Kripya code ko 'Play' button se nahi, balki terminal mein"
        " 'python Collection_data.py' likh kar chalayein!"
    )
    break
  except ValueError:
    print("Kripya ek valid number daalein!")
    continue

  if choice == 0:
    print("Data collection band ho gaya. All the best for your hackathon!")
    break

  choice -= 1  # Indexing fix (1 -> 0)
  if choice < 0 or choice >= len(gestures):
    print("Galat number! Kripya 1 se 12 ke beech ka number chunein.")
    continue

  gesture_name = gestures[choice]
  TARGET_SAMPLES = 150
  count = 0

  print(f"\n--- Recording Started for: {gesture_name.upper()} ---")
  print("Camera open ho raha hai. Gesture karein (150 samples collect honge)...")

  cap = cv2.VideoCapture(0)

  while cap.isOpened():
    success, frame = cap.read()
    if not success:
      print("Camera frame nahi mila.")
      break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    # Fix 126 features (2 hands * 21 landmarks * 3 coordinates)
    row = [0.0] * (2 * 21 * 3)

    if results.multi_hand_landmarks:
      for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
        if idx < 2:
          mp_draw.draw_landmarks(
              frame, hand_landmarks, mp_hands.HAND_CONNECTIONS
          )
          start_idx = idx * 21 * 3
          for lm_idx, lm in enumerate(hand_landmarks.landmark):
            row[start_idx + (lm_idx * 3)] = lm.x
            row[start_idx + (lm_idx * 3) + 1] = lm.y
            row[start_idx + (lm_idx * 3) + 2] = lm.z

      row_with_label = row + [gesture_name]

      with open("dataset.csv", mode="a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(row_with_label)

      count += 1

    # Screen par live status dikhana
    cv2.putText(
        frame,
        f"Target: {gesture_name.upper()} ({count}/{TARGET_SAMPLES})",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )
    cv2.putText(
        frame,
        "Press 'q' to stop this gesture",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (0, 0, 255),
        2,
    )

    cv2.imshow("ISL Data Collection", frame)

    if count >= TARGET_SAMPLES:
      print(f"\n'{gesture_name}' ke {TARGET_SAMPLES} samples poore ho gaye!")
      break

    if cv2.waitKey(1) & 0xFF == ord("q"):
      print(f"\n'{gesture_name}' collection beech mein rok di gayi.")
      break

  cap.release()
  cv2.destroyAllWindows()
  print(f"'{gesture_name}' session finished. Wapas menu par ja rahe hain...\n")