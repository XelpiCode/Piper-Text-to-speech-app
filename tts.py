import subprocess
import tempfile
import os
from pathlib import Path

VOICE = "voices/en_US-hfc_female-medium.onnx"
MP3_DIR = Path("mp3")

def next_mp3_name() -> Path:
    MP3_DIR.mkdir(exist_ok=True)

    existing = sorted(MP3_DIR.glob("*.mp3"))
    if not existing:
        return MP3_DIR / "0001.mp3"

    last = int(existing[-1].stem)
    return MP3_DIR / f"{last + 1:04d}.mp3"


def speak(text: str):
    mp3_path = next_mp3_name()

    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        wav_path = tmp.name

    try:
        # 1️⃣ Generate WAV using Piper
        subprocess.run(
            ["piper", "--model", VOICE, "--output_file", wav_path],
            input=text,
            text=True,
            check=True
        )

        # 2️⃣ Convert WAV → MP3 using ffmpeg
        subprocess.run(
            [
                "ffmpeg", "-y",
                "-loglevel", "error",
                "-i", wav_path,
                str(mp3_path)
            ],
            check=True
        )

        print(f"Saved: {mp3_path}")

    finally:
        # 3️⃣ Always delete WAV
        if os.path.exists(wav_path):
            os.remove(wav_path)
