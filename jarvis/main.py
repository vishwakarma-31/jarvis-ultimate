import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import threading
import keyboard

from voice.listener import listen_for_command  # ✅ Correct: it's a function
from jarvis.voice.speaker import VoiceSpeaker
from jarvis.core.brain import GPTBrain
from jarvis.core.memory import MemoryLogger
from jarvis.system.control import SystemController
from jarvis.gui.panel import JarvisGUI

class JarvisCore:
    def __init__(self):
        self.speaker = VoiceSpeaker()
        self.gpt = GPTBrain()
        self.memory = MemoryLogger()
        self.system = SystemController()
        self.gui_state = {
            "listening": False,
            "last_command": "",
            "last_response": ""
        }
        self.gui = JarvisGUI(self.gui_state)

    def background_jarvis(self):
        while True:
            # ✅ Call the function directly
            command = listen_for_command()

            if not command:
                continue

            self.gui_state["last_command"] = command

            if self.system.handle(command):
                response = f"Executed: {command}"
            else:
                response = self.gpt.process(command)

            self.gui_state["last_response"] = response
            self.memory.log(command, response)
            self.speaker.speak(response)

    def run(self):
        # Start assistant logic in background
        jarvis_thread = threading.Thread(target=self.background_jarvis, daemon=True)
        jarvis_thread.start()

        # Run GUI on main thread (required by tkinter)
        self.gui.run()

    def watch_for_stop(self):
        # Allows ESC key to stop speaking
        keyboard.add_hotkey("esc", lambda: self.speaker.stop())

if __name__ == "__main__":
    print("🧠 JARVIS starting up...")
    jarvis = JarvisCore()
    jarvis.run()
    jarvis.watch_for_stop()
