from tkinter import Tk
import sys
import os
import threading
import keyboard

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from voice.listener import listen_for_command
from jarvis.voice.speaker import VoiceSpeaker
from jarvis.core.brain import GPTBrain
from jarvis.core.memory import MemoryLogger
from jarvis.system.control import SystemController
from jarvis.gui.panel import JarvisGUI


class JarvisCore:
    def __init__(self):
        # ✅ Initialize all core modules
        self.speaker = VoiceSpeaker()
        self.gpt = GPTBrain()
        self.memory = MemoryLogger()
        self.system = SystemController()

        # ✅ GUI state for sharing between backend and GUI
        self.gui_state = {
            "listening": False,
            "last_command": "",
            "last_response": ""
        }

        # ✅ Initialize GUI
        self.root = Tk()
        self.gui = JarvisGUI(self.root, self.gui_state)

    def background_jarvis(self):
        while True:
            command = listen_for_command()

            if not command:
                continue

            self.gui_state["last_command"] = command

            # First try system action
            success = self.system.handle(command)

            if success:
                response = f"Executed: {command}"
            else:
                # Fallback to LLM (Ollama or OpenAI)
                response = self.gpt.process(command)
                response += " — but I couldn't execute that on your system."

            self.gui_state["last_response"] = response
            self.memory.log(command, response)
            self.speaker.speak(response)

    def run(self):
        jarvis_thread = threading.Thread(target=self.background_jarvis, daemon=True)
        jarvis_thread.start()
        self.gui.run()

    def watch_for_stop(self):
        keyboard.add_hotkey("esc", lambda: self.speaker.stop())


if __name__ == "__main__":
    print("🧠 JARVIS starting up...")
    jarvis = JarvisCore()
    jarvis.run()
    jarvis.watch_for_stop()
