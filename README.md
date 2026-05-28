# Echo Motion: AI-Powered Sign Language Assistant
# USE PYTHON VERSION 3.12

Streamlit Website URL is: https://echomotionai.streamlit.app

A sign language and gesture-based AI assistant that connects sign language and computer interaction is Echo Motion. It translates finger patterns into complex hands-free system commands, web searches, and natural language conversations using computer vision and large language models (LLMs).

## Tech Stack

* **Language:** Python 3.12
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

## The Gesture Map (Hand Dictionary)

It uses a  binary state system `(Thumb, Index, Middle, Ring, Pinky)` where `1` is open and `0` is closed.

You can view the map its in the website on the sidebar.

## AI was just used for code debugging purposes.


