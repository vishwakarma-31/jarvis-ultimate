import tkinter as tk
from tkinter import messagebox
import threading
from jarvis.system.control import SystemController

class JarvisGUI:
    def __init__(self, root, gui_state):
        self.root = root
        self.gui_state = gui_state
        self.root.title("Jarvis AI Assistant")
        self.root.geometry("400x500")
        self.controller = SystemController()

        self.label = tk.Label(root, text="Jarvis Dashboard", font=("Helvetica", 18, "bold"))
        self.label.pack(pady=20)

        # Define commands
        self.commands = {
            "Open Chrome": "open chrome",
            "Open File Explorer": "open file explorer",
            "Take Screenshot": "take screenshot",
            "Type Hello World": "type hello world",
            "Mouse Position": "where is my mouse",
            "Shutdown": "shutdown"
        }

        for btn_text, cmd in self.commands.items():
            tk.Button(root, text=btn_text, font=("Helvetica", 12), width=25, pady=5,
                      command=lambda c=cmd: self.run_command(c)).pack(pady=5)

        self.log = tk.Text(root, height=10, width=45)
        self.log.pack(pady=10)
        self.log.insert(tk.END, "Jarvis is ready...\\n")

    def run_command(self, command):
        def threaded():
            self.log.insert(tk.END, f"\n>> {command}\n")
            success = self.controller.handle(command)
            if success:
                self.log.insert(tk.END, "✅ Command executed successfully.\n")
            else:
                self.log.insert(tk.END, "❌ Command failed or not recognized.\n")
        threading.Thread(target=threaded).start()


    def run(self):
        self.root.mainloop()
