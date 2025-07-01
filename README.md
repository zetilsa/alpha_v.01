# 🎙️ Indonesian Voice Assistant

An Indonesian-language voice assistant written in Python, able to listen for voice commands and execute simple tasks like opening websites, taking screenshots, managing task lists, and speaking responses using text-to-speech.

---

## ✨ Features

✅ Trigger word recognition (e.g. "alfa" or "alpha")  
✅ Understands Indonesian voice commands  
✅ Responds with Indonesian speech (gTTS)  
✅ Open YouTube in your browser  
✅ Take a screenshot and save it locally  
✅ Answer predefined questions about its creator or purpose  
✅ Add tasks to a personal task list  
✅ Read out all saved tasks  
✅ Exit via voice command

---

## 🎧 How It Works

- Waits for the user to say the trigger word (e.g. "alfa").
- After being triggered, it listens for specific commands.
- Recognizes Indonesian speech using Google Speech Recognition API.
- Speaks responses using Google Text-to-Speech (gTTS).
- Converts audio files for playback on Windows (MP3 → WAV).
- Supports basic task management via voice.

---

## 🛠️ Requirements

- Python 3.x
- Windows OS (uses `winsound`)
- Microphone
- Internet connection (for Google Speech Recognition and gTTS)

Python Libraries:
- speech_recognition
- gTTS
- pydub
- pyautogui
- webbrowser

External Tools:
- FFmpeg (for pydub audio conversion)

---

## ⚙️ Installation

1. **Clone the repository:**

    ```bash
    git clone <your-repo-url>
    cd <your-repo-folder>
    ```

2. **Install Python dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    Example requirements.txt:
    ```
    SpeechRecognition
    gTTS
    pydub
    pyautogui
    ```

3. **Install FFmpeg:**

    - Download from: https://ffmpeg.org/download.html
    - Add `ffmpeg` and `ffprobe` executables to your system PATH.

---

## 🚀 Running the Assistant

Run the script:

```bash
python your_script_name.py
