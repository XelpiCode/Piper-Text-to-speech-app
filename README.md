# PiperTTS (Offline Text-to-Speech → MP3)

A **simple offline Text-to-Speech CLI tool** using **Piper TTS**.
It converts text into speech, **plays the audio instantly**, and **saves it as an MP3**.

---

## ✨ Features

* Fully **offline TTS** (no API, no internet)
* Uses **Piper** ONNX voices
* Automatically:

  * Creates the `mp3/` folder
  * Numbers MP3 files (`0001.mp3`, `0002.mp3`, ...)
* Plays audio immediately after generation
* Clean CLI interface

---

## 📂 Project Structure

```
PiperTTS/
├── mp3/                      # Generated MP3 files
├── voices/                   # Piper ONNX voice models
│   ├── en_US-hfc_female-medium.onnx
│   ├── en_US-hfc_female-medium.onnx.json
│   ├── en_US-kusal-medium.onnx
│   └── en_US-kusal-medium.onnx.json
├── cli.py                    # CLI entry point
├── tts.py                    # TTS logic
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔧 Requirements

### 1️⃣ System Requirements

* **Python 3.10+**
* **FFmpeg** (must be in PATH)
* **Piper TTS** installed and accessible as `piper`

#### Install FFmpeg

**Windows (winget)**

```bash
winget install Gyan.FFmpeg
```

**Linux (Arch)**

```bash
sudo pacman -S ffmpeg
```

---

### 2️⃣ Install Piper

```bash
pip install piper-tts
```

Verify:

```bash
piper --help
```

---

### 3️⃣ Python Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔊 Voices Setup

1. Download voices from the Piper HuggingFace repo:

   * [https://huggingface.co/rhasspy/piper-voices](https://huggingface.co/rhasspy/piper-voices)

2. Place both files in the `voices/` folder:

   * `*.onnx`
   * `*.onnx.json`

Example:

```
voices/
├── en_US-hfc_female-medium.onnx
├── en_US-hfc_female-medium.onnx.json
```

> ⚠️ The `.json` file is required — it contains metadata Piper needs.

---

## ▶️ Usage

From the project root:

```bash
python cli.py "Hello world, this is offline text to speech"
```

What happens:

1. Text is converted to WAV using Piper
2. Audio is played instantly
3. WAV is converted to MP3
4. MP3 is saved in `mp3/`

Example output:

```
Saved: mp3/0001.mp3
```

---

## 🎙 Changing the Voice

Edit `tts.py`:

```python
VOICE = "voices/en_US-hfc_female-medium.onnx"
```

Change it to any other ONNX voice you have.

---

## 🧠 How It Works

1. Piper generates a temporary WAV file
2. `sounddevice` plays the WAV
3. FFmpeg converts WAV → MP3
4. Temporary files are cleaned automatically

---

## 🧹 Cleanup

Temporary WAV files are deleted automatically after conversion.

---

## 📜 License

MIT License

---

## ⭐ Notes

* Fully offline
* Fast startup
* Great for scripts, automation, and local assistants

___