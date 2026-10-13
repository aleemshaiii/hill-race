# 🏎️ Hill Climb CV Controller

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)
![MediaPipe](https://img.shields.io/badge/MediaPipe-1.0.1-orange.svg)

A real-time Computer Vision controller for **Hill Climb Racing**. This project uses your webcam and Google's MediaPipe hand-tracking to translate physical hand gestures into virtual keyboard strokes, allowing you to drive the car entirely hands-free.

## ✨ Features
* **Real-Time Hand Tracking:** Utilizes MediaPipe's modern Tasks API for low-latency landmark detection.
* **Gesture Mapping:** 
  * 🖐️ **Open Hand (3-4 fingers):** Accelerate (Right Arrow)
  * ✊ **Closed Fist (0 fingers):** Brake/Reverse (Left Arrow)
  * ✌️ **Peace Sign (2 fingers):** Restart Level (Enter)
* **Auto-Provisioning:** Automatically downloads the required MediaPipe `.task` model file on the first run.
* **Fail-safe Integration:** Uses `pyautogui` to seamlessly simulate hardware-level keystrokes.

## ⚙️ Installation

1. **Clone the repository:**
bash
git clone https://github.com/aleemshaiii/hill-race.git
cd hill-race

2. **Create and activate a virtual environment:**
bash
python -m venv venv
.\venv\Scripts\activate  # Windows

3. **Install dependencies:**
bash
pip install -r requirements.txt

## 🚀 Usage

1. Launch **Hill Climb Racing** on your PC and get to the starting line.
2. Run the vision controller:bash
python main.py
3. **CRITICAL:** Click on the Hill Climb Racing game window with your mouse so it is active. 
4. Hold your hand up to the webcam and start driving! 

*(To quit, click the camera window and press the `q` key).*

## 📂 Architecture
* `main.py`: The core execution loop, handling the camera feed and `pyautogui` keystroke simulation.
* `tracker.py`: The vision engine utilizing `mediapipe` to calculate hand landmarks and determine gestures via finger-joint heuristics.