# JARVIS: Personal Voice Assistant (Offline, Modular)

JARVIS is a modular, offline-first voice assistant for Windows using:
- 🔊 Voice input/output via `SpeechRecognition` & `pyttsx3`
- 🧠 Local AI via `ollama` (LLaMA 3)
- 🛠️ System control: open apps, change volume/brightness
- 🗃️ Encrypted memory logger
- 📊 GUI panel for logs and control

## 🧩 Features
- Wake word: “Jarvis” to activate
- British male TTS
- LLaMA 3 local GPT processing
- System-level actions: open VS Code, mute audio, brightness
- Encrypted memory with timestamped logs
- Custom macros (via `macros.json`)

## 🔧 Setup
1. Clone repo or unzip
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python jarvis/main.py
   ```

## 🔒 Logs
All logs are stored encrypted in `logs/jarvis_log.enc` and can only be read using `MemoryLogger`.

## 🎙️ Voice Commands (Examples)
- “Jarvis open chrome”
- “Jarvis increase volume”
- “Jarvis shut down the system”
- “Jarvis what’s the capital of Italy?”

---