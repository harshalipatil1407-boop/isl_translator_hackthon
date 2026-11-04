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
### Detailed Execution Pipeline
1. **Video Capture & Landmarking:** OpenCV captures real-time video frames (30 FPS). MediaPipe Hand Landmarker extracts **21 three-dimensional coordinates (x, y, z)** per hand, totaling **42 landmark coordinates** per frame.
2. **Feature Vector Processing:** Spatial coordinates are normalized relative to hand bounding boxes to ensure scale and distance invariance.
3. **Machine Learning Inference:** The feature vector is evaluated against a pre-trained **Random Forest Classifier** trained on custom ISL gesture samples.
4. **Debounce & Cooldown Logic:** An automated temporal threshold filter validates gesture stability over successive frames before committing predictions.
5. **Non-Blocking Speech Output:** A native **PowerShell System.Speech** execution bridge handles text-to-speech asynchronously, preventing webcam frame drops.

---

## 🛠️ Complete Tech Stack

| Component | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core application logic and pipeline management |
| **Computer Vision** | OpenCV (`cv2`) | Video stream capture, image processing, UI overlay rendering |
| **Hand Tracking** | MediaPipe | Real-time 3D hand landmark localization (21 keypoints) |
| **Machine Learning** | Scikit-Learn | Random Forest Classifier training and prediction engine |
| **Data Serialization** | Joblib / Pickle | Serialized storage and fast loading of trained model weights |
| **Speech Engine** | Windows PowerShell (`System.Speech`) | Native asynchronous text-to-speech synthesis without blocking UI |

---

## ⚙️ Key Technical Features & Innovation

* **Zero-Touch Automation:** Hands-free execution without needing keyboard or mouse triggers.
* **Asynchronous Audio Pipeline:** Solved the common `pyttsx3` thread lock issue by decoupling audio processing using native PowerShell commands.
* **High-Accuracy Classification:** Optimized Random Forest model achieving high precision across single-word ISL signs under variable indoor lighting.
* **Low Computational Overhead:** Lightweight landmark-based feature extraction running smoothly at 30+ FPS on CPU without needing dedicated GPU hardware.

---

## 🔮 Future Scope & Roadmap

While the current MVP successfully translates real-time single-word ISL gestures into continuous speech, our long-term vision includes:
* **Full Sentence Formation & Speech Synthesis:** Developing dynamic sequence recognition to stitch continuous single-word ISL signs into grammatically coherent, fluid spoken sentences in real-time.
* **Grammar & Context Correction:** Integrating lightweight LLMs to structure raw predicted sign tokens into natural native language sentence flows.
* **Mobile & Web Deployment:** Converting the desktop pipeline into a lightweight web and mobile app using TensorFlow.js / ONNX runtime for universal accessibility.

---

## 🚀 Setup & Installation Guide

### Prerequisites
* Windows 10 / 11 OS
* Python 3.8 or higher
* Integrated or external USB Webcam

### 1. Repository Setup
```bash
git clone [https://github.com/harshalipatil1407-boop/isl_translator_hackathon.git](https://github.com/harshalipatil1407-boop/isl_translator_hackathon.git)
cd isl_translator_hackathon
