import ollama

class GPTBrain:
    def __init__(self):
        self.model = "llama3"

    def process(self, command: str) -> str:
        try:
            print("[LLaMA] Processing command...")
            response = ollama.chat(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                    {"role": "user", "content": command}
                ]
            )
            return response['message']['content']
        except Exception as e:
            print(f"[LLaMA ERROR] {e}")
            return "Sorry, I couldn't process that command."