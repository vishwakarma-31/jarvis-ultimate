import os
import json
from datetime import datetime
from jarvis.core.encryptor import encrypt_data, decrypt_data

MEMORY_FILE = "logs/jarvis_log.enc"

class MemoryLogger:
    def log(self, command: str, response: str):
        log = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "command": command,
            "response": response
        }

        existing_logs = []
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, "rb") as f:
                    decrypted = decrypt_data(f.read())
                    existing_logs = json.loads(decrypted)
            except Exception as e:
                print(f"[Memory] Failed to read previous memory: {e}")

        existing_logs.append(log)
        try:
            encrypted = encrypt_data(json.dumps(existing_logs, indent=2))

            # ✅ Ensure the logs/ folder exists before writing
            os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)

            with open(MEMORY_FILE, "wb") as f:
                f.write(encrypted)
        except Exception as e:
            print(f"[Memory] Failed to write memory: {e}")

    def get_logs(self, limit=5):
        if not os.path.exists(MEMORY_FILE):
            return []
        try:
            with open(MEMORY_FILE, "rb") as f:
                decrypted = decrypt_data(f.read())
                all_logs = json.loads(decrypted)
                return all_logs[-limit:]
        except Exception as e:
            print(f"[Memory] Failed to load memory logs: {e}")
            return []
