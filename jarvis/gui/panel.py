import tkinter as tk
from tkinter import scrolledtext

class JarvisGUI:
    def __init__(self, state):
        self.state = state
        self.root = tk.Tk()
        self.root.title("JARVIS AI Assistant")
        self.root.geometry("420x320")
        self.root.configure(bg="#0F1117")
        self.root.resizable(False, False)

        self.header = tk.Label(self.root, text="🤖 JARVIS CONTROL PANEL", font=("Segoe UI", 14, "bold"), bg="#0F1117", fg="#00FFAA")
        self.header.pack(pady=10)

        self.status_label = tk.Label(self.root, text="Status: Idle", font=("Segoe UI", 12), bg="#0F1117", fg="white")
        self.status_label.pack()

        self.log_box = scrolledtext.ScrolledText(self.root, height=10, width=48, wrap=tk.WORD, font=("Segoe UI", 10), bg="#1A1C22", fg="#00FFAA")
        self.log_box.pack(pady=10)
        self.log_box.insert(tk.END, ">> Jarvis initialized.\n")
        self.log_box.config(state=tk.DISABLED)

        button_frame = tk.Frame(self.root, bg="#0F1117")
        button_frame.pack(pady=10)

        self.listen_btn = tk.Button(button_frame, text="🎤 Toggle Listening", command=self.toggle_listening, width=18, bg="#006699", fg="white", font=("Segoe UI", 10))
        self.listen_btn.pack(side=tk.LEFT, padx=10)

        self.exit_btn = tk.Button(button_frame, text="❌ Exit", command=self.root.destroy, width=10, bg="#CC3333", fg="white", font=("Segoe UI", 10))
        self.exit_btn.pack(side=tk.RIGHT, padx=10)

        self.update_gui()

    def toggle_listening(self):
        self.state["listening"] = not self.state["listening"]
        status = "Listening..." if self.state["listening"] else "Idle"
        self.status_label.config(text=f"Status: {status}")

    def update_gui(self):
        if self.state["last_command"]:
            self.append_log(f"You said: {self.state['last_command']}")
            self.state["last_command"] = ""

        if self.state["last_response"]:
            self.append_log(f"Jarvis: {self.state['last_response']}")
            self.state["last_response"] = ""

        if self.state.get("listening"):
            self.status_label.config(text="Status: Listening...")
        else:
            self.status_label.config(text="Status: Idle")

        self.root.after(1000, self.update_gui)

    def append_log(self, message: str):
        self.log_box.config(state=tk.NORMAL)
        self.log_box.insert(tk.END, f">> {message}\n")
        self.log_box.see(tk.END)
        self.log_box.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()
