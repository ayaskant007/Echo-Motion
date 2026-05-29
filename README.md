# Echo Motion: AI-Powered Sign Language Assistant

Streamlit Website URL is: https://echomotionai.streamlit.app
Demo Video URL is: 

A sign language and gesture-based AI assistant that connects sign language and computer interaction is Echo Motion. It translates finger patterns into complex hands-free system commands, web searches, and natural language conversations using computer vision and large language models (LLMs).

## Features

* **32-Gesture Control:** Works by using the binary finger state map (Thumb to Pinky) for 32 unique gestures.
* **Integration with Gemini AI:** Employs gemini-3-flash to convert raw signs into useful sentences.
* **Web Interface:** A modern interface designed using Streamlit which provides chat logs and camera stream functionality.
* **Multi-threading Audio (Jarvis):** Specialized Windows Speech to Text Integration enabling Jarvis to talk while video processing does not pause.
* **Entertainment:** Ability to play any YouTube song using pywhatkit.
* **Information:** Access live news using News API and current weather reports.
* **Internet:** Quick navigation to Google, Facebook, and YouTube. (Provides direct  button links on the streamlit page)

## Tech Stack

* **Language:** Python 3.12 (Any other versions won't work due to the mediapipe dependency not working on other python versions)
* **Vision:** OpenCV, MediaPipe for capturing image/video and recognizing hand patterns.
* **Frontend:** Streamlit for the website ui/ux (frontend)
* **Audio:** Win32Com, which is basically the built-in windows text to speech
* **APIs:** NewsAPI for fetching the news, Google GenAI for gemini

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ayaskant007/Echo-Motion.git
cd Echo-Motion
```

### 2. Create a .venv for installing the pip modules
```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python -m streamlit run "app.py"
```

or just visit the Streamlit link!

---

**You can see the gesture map its in the side bar of the website.**
**AI was just used for code debugging purposes.**
