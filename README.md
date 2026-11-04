# Real-Time Indian Sign Language (ISL) Translator

An automated, hands-free computer vision framework designed to bridge the communication gap between speech/hearing-impaired individuals and the general public by converting real-time Indian Sign Language (ISL) gestures into visual text and continuous vocal output.

---

 Project & Team Overview
* **Challenge Track:** Human Impact
* **Project Name:** Indian Sign Language (ISL) Real-Time Translator
* **Team Name:** Harshali Patil & Team
* **Target Audience:** Non-verbal individuals, educators, healthcare professionals, and public service personnel.

---

 Problem Statement & Real-World Impact
Over 1.8 million people in India rely on Indian Sign Language (ISL) as their primary mode of communication. However, a significant gap exists due to a lack of widespread ISL literacy among the general public. 

Existing vision-based translation solutions often face key operational bottlenecks:
1. **Manual Interventions:** Requiring users to press keys (e.g., Spacebar) to trigger speech synthesis.
2. **Audio Overlapping & Stuttering:** Frequent TTS engine re-initialization causing audio buffer overflows.
3. **High Latency & Resource Consumption:** Heavy deep learning models struggling on standard webcam hardware.

### Our Solution
Our system provides a **fully automated, hands-free end-to-end pipeline** that detects sign language gestures from standard webcam feeds, classifies gestures using high-dimensional landmark geometry, and speaks the translated output asynchronously without UI freezing or speech repetition.

---

## 🏗️ System Architecture & Workflow
