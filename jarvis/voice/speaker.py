import pyttsx3
import threading

class VoiceSpeaker:
    def __init__(self):
        self.engine = pyttsx3.init()
        self._set_british_male()
        self.engine.setProperty('rate', 185)
        self.lock = threading.Lock()

    def _set_british_male(self):
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'english' in voice.name.lower() and 'male' in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                return

    def speak(self, text: str):
        print(f"[TTS] Speaking: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    def stop(self):
        with self.lock:
            print("[TTS] Stopping speech...")
            self.engine.stop()