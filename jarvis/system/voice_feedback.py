import pyttsx3

class VoiceFeedback:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)  # Speed of speech
        self.engine.setProperty('volume', 1.0)  # Max volume

    def speak(self, text: str):
        try:
            self.engine.say(text)
            self.engine.runAndWait()
        except Exception as e:
            print(f"Voice engine error: {e}")
