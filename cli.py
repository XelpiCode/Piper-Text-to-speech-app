import argparse
from tts import speak

def main():
    parser = argparse.ArgumentParser(description="Offline Piper TTS → MP3")
    parser.add_argument("text", help="Text to convert to speech")
    args = parser.parse_args()

    speak(args.text)

if __name__ == "__main__":
    main()
