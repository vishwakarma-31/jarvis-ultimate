### ❓ What is this project?
A modular offline AI voice assistant with full system control, voice recognition, LLaMA-based processing, GUI, and encrypted memory.

### ❓ How is the voice handled?
`SpeechRecognition` captures the mic input, checks for wake word, and then transcribes the audio to text. The assistant responds using `pyttsx3` TTS.

### ❓ What is the role of `ollama`?
It connects to a local running LLaMA 3 model via API and returns context-aware GPT-style responses without internet.

### ❓ How does encryption work?
A symmetric Fernet key (`jarvis.key`) is generated and used to encrypt/decrypt JSON logs using `cryptography`.

### ❓ How are system commands handled?
Custom logic in `SystemController` maps phrases like “open chrome” to `subprocess.Popen()` calls. Brightness and volume use `pyautogui` or `powershell`.

### ❓ How to add new commands?
Add phrases to `SystemController.handle()` or create new macros in `macros.json`.

### ❓ How is memory stored?
In encrypted form inside `logs/jarvis_log.enc` using the `MemoryLogger` class.

### ❓ How is the GUI implemented?
A simple `Tkinter` interface with status, scrolling log, and buttons to toggle listening or exit.

---
You’re now interview-ready! ✅
