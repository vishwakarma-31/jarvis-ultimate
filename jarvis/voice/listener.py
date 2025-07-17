# Handles voice input

import speech_recognition as sr

# Recognizer instance (shared across calls)
recognizer = sr.Recognizer()

def listen_for_command(wake_word: str = "jarvis") -> str:
    """
    Listen for a command from the user's microphone.
    If a wake word is specified, the assistant will only respond after hearing it.
    Returns the recognized command as lowercase text.
    """
    try:
        with sr.Microphone(device_index=1) as source:
            print("[Mic] Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("[Mic] Listening... 🎤")

            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)

            print("[Mic] Processing...")
            query = recognizer.recognize_google(audio)  # type: ignore[attr-defined]
            query = query.lower()

            if wake_word:
                if wake_word in query:
                    print(f"[Wake Word Detected] {query}")
                    return query.replace(wake_word, "").strip()
                else:
                    print("[Wake Word Not Detected]")
                    return ""
            else:
                return query

    except sr.UnknownValueError:
        print("[Mic] Could not understand audio.")
        return ""
    except sr.RequestError as e:
        print(f"[Mic] API request error: {e}")
        return ""
    except sr.WaitTimeoutError:
        print("[Mic] Listening timed out.")
        return ""
    except Exception as e:
        print(f"[Mic] Error: {e}")
        return ""
