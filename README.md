# Real-Time Indian Sign Language (ISL) Translator

An automated, hands-free computer vision framework designed to bridge the communication gap between speech/hearing-impaired individuals and the general public by converting real-time Indian Sign Language (ISL) gestures into visual text and continuous vocal output.

---

## Project & Team Overview
* **Challenge Track:** Human Impact
* **Project Name:** Indian Sign Language (ISL) Real-Time Translator
* **Team Name:** Hackuno
* **Target Audience:** Non-verbal individuals, educators, healthcare professionals, and public service personnel.

---

##  Problem Statement & Real-World Impact
Over 1.8 million people in India rely on Indian Sign Language (ISL) as their primary mode of communication. However, a significant gap exists due to a lack of widespread ISL literacy among the general public. 

Existing vision-based translation solutions often face key operational bottlenecks:
1. **Manual Interventions:** Requiring users to press keys (e.g., Spacebar) to trigger speech synthesis.
2. **Audio Overlapping & Stuttering:** Frequent TTS engine re-initialization causing audio buffer overflows.
3. **High Latency & Resource Consumption:** Heavy deep learning models struggling on standard webcam hardware.

### Our Solution
Our system provides a **fully automated, hands-free end-to-end pipeline** that detects sign language gestures from standard webcam feeds, classifies gestures using high-dimensional landmark geometry, and speaks the translated output asynchronously without UI freezing or speech repetition. This Currently working on gestures like( hello,bye,water,eat,no,help,need,pain,good/ok,stop,washroom)

---

## System Architecture & Workflow
### Detailed Execution Pipeline
1. **Video Capture & Landmarking:** OpenCV captures real-time video frames (30 FPS) with optimized color-space mapping (BGR to RGB). MediaPipe Hand Landmarker extracts **21 three-dimensional coordinates (x, y, z)** per hand, totaling **42 landmark coordinates** per frame.
2. **Advanced Feature Vector Processing & Normalization:** Spatial coordinates are translated relative to wrist anchor points ($x_0, y_0, z_0$) and normalized against bounding box diagonal dimensions to ensure complete scale and distance invariance from the webcam sensor.
3. **Machine Learning Inference:** The structured 42-dimensional feature vector is evaluated against a pre-trained **Random Forest Classifier** ensemble optimized for low-latency multi-class gesture classification.
4. **Temporal Debounce & Cooldown Logic:** An automated sliding window state machine validates gesture stability over consecutive frames and enforces a strict timestamp cooldown buffer to prevent erratic multi-triggering.
5. **Asynchronous Non-Blocking Speech Output:** Bypasses standard blocking thread locks (such as traditional `pyttsx3` freezes) by leveraging a native **PowerShell System.Speech** asynchronous subprocess execution bridge.

---

##  Complete Tech Stack

| Component | Technology / Library | Purpose |
| :--- | :--- | :--- |
| **Language** | Python 3.10+ | Core application logic and pipeline management |
| **Computer Vision** | OpenCV (`cv2`) | Video stream capture, image processing, UI overlay rendering |
| **Hand Tracking** | MediaPipe | Real-time 3D hand landmark localization (21 keypoints per hand) |
| **Machine Learning** | Scikit-Learn | Random Forest Classifier training, multi-class evaluation, and model inference |
| **Data Serialization** | Joblib / Pickle | Serialized pipeline storage for ultra-fast model loading and low memory footprint |
| **Speech Engine** | Windows PowerShell (`System.Speech`) | Native asynchronous text-to-speech synthesis without blocking the main event loop |

---

##  Key Technical Features & Innovation

* **Zero-Touch Automation:** Fully hands-free real-time execution operating entirely without keyboard or mouse overrides.
* **Asynchronous Audio Concurrency:** Solved standard Python audio thread lockouts by decoupling speech generation into isolated PowerShell background execution processes.
* **High-Precision Spatial Inference:** Robust Random Forest model tuned to maintain high classification accuracy under variable indoor lighting conditions.
* **Optimized CPU Performance:** Lightweight geometric feature extraction running smoothly at 30+ frames per second on standard CPU configurations without requiring dedicated GPU accelerators.

---

##  Future Scope & Roadmap

While the current MVP successfully translates real-time single-word ISL gestures into continuous speech, our long-term technical vision includes:
* **Full Sentence Formation & Speech Synthesis:** Developing dynamic sequence recognition models (such as LSTMs or lightweight temporal transformers) to stitch continuous single-word ISL signs into grammatically coherent, fluid spoken sentences in real-time.
* **Grammar & Context Correction:** Integrating lightweight local LLM wrappers to structure raw predicted sign tokens into natural native language sentence flows.
* **Mobile & Web Deployment:** Converting the desktop pipeline into a lightweight web and cross-platform mobile app using TensorFlow.js / ONNX runtime.

---

##  Setup & Installation Guide

### Prerequisites
* Windows 10 / 11 OS
* Python 3.8 or higher
* Integrated or external USB Webcam

### 1. Repository Setup
```bash
git clone [https://github.com/harshalipatil1407-boop/isl_translator_hackthon.git](https://github.com/harshalipatil1407-boop/isl_translator_hackthon.git)
cd isl_translator_hackthon
