import os
import subprocess
import pyautogui
import platform

from .automation import AutomationController
from .advanced_automation import AdvancedAutomation
from .voice_feedback import VoiceFeedback

class SystemController:
    def __init__(self):
        self.automation = AutomationController()
        self.advanced = AdvancedAutomation()
        self.voice = VoiceFeedback()

    def handle(self, command: str) -> bool:
        command = command.lower()

        if "open" in command:
            if self._launch_app(command):
                self.voice.speak("Opening application")
                return True

        if "close" in command:
            if self._close_app(command):
                self.voice.speak("Closing application")
                return True

        if "volume" in command:
            if self._adjust_volume(command):
                self.voice.speak("Adjusting volume")
                return True

        if "brightness" in command:
            if self._adjust_brightness(command):
                self.voice.speak("Adjusting brightness")
                return True

        if "shutdown" in command:
            self.voice.speak("Shutting down the system")
            os.system("shutdown /s /t 1")
            return True

        if "restart" in command:
            self.voice.speak("Restarting the system")
            os.system("shutdown /r /t 1")
            return True

        if "lock" in command:
            self.voice.speak("Locking the system")
            os.system("rundll32.exe user32.dll,LockWorkStation")
            return True

        if "sleep" in command:
            self.voice.speak("Putting system to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            return True

        if "type" in command:
            text = command.replace("type", "").strip()
            response, ok = self.advanced.type_text(text)
            print(response)
            self.voice.speak(response if ok else "Failed to type")
            return ok

        if "press control s" in command:
            result = self.automation.press_hotkey("ctrl", "s")
            print(result)
            self.voice.speak("Pressed Control S")
            return True

        if "move mouse to center" in command:
            screen_width, screen_height = pyautogui.size()
            result = self.automation.move_mouse(screen_width // 2, screen_height // 2)
            print(result)
            self.voice.speak("Mouse moved to center")
            return True

        if "click" in command:
            clicks = 2 if "double" in command else 1
            result = self.automation.click_mouse(clicks=clicks)
            print(result)
            self.voice.speak("Mouse clicked")
            return True

        if "scroll up" in command:
            print(self.automation.scroll_mouse(500))
            self.voice.speak("Scrolling up")
            return True

        if "scroll down" in command:
            print(self.automation.scroll_mouse(-500))
            self.voice.speak("Scrolling down")
            return True

        if "take screenshot" in command:
            response, ok = self.advanced.take_screenshot("screenshot.png")
            print(response)
            self.voice.speak(response if ok else "Failed to take screenshot")
            return ok

        if "where is my mouse" in command or "mouse position" in command:
            response, ok = self.advanced.get_mouse_position(), True
            print(response)
            self.voice.speak(response)
            return ok

        return False

    def _launch_app(self, command: str) -> bool:
        apps = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "notepad": "notepad",
            "file explorer": "explorer",
            "vs code": "code",
            "calculator": "calc",
            "edge": "msedge",
            "task manager": "taskmgr",
            "settings": "start ms-settings:",
            "control panel": "control",
            "cmd": "cmd"
        }

        for key, path in apps.items():
            if key in command:
                try:
                    if os.path.exists(path):
                        os.startfile(path)
                    else:
                        subprocess.Popen(path, shell=True)
                    return True
                except Exception as e:
                    print(f"Failed to open {key}: {e}")
                    return False
        return False

    def _close_app(self, command: str) -> bool:
        app_names = {
            "chrome": "chrome.exe",
            "notepad": "notepad.exe",
            "vs code": "Code.exe",
            "calculator": "Calculator.exe",
            "edge": "msedge.exe",
            "task manager": "Taskmgr.exe"
        }

        for key, process in app_names.items():
            if key in command:
                try:
                    os.system(f"taskkill /f /im {process}")
                    return True
                except Exception as e:
                    print(f"Failed to close {key}: {e}")
                    return False
        return False

    def _adjust_volume(self, command: str) -> bool:
        try:
            if "up" in command:
                pyautogui.press("volumeup")
            elif "down" in command:
                pyautogui.press("volumedown")
            elif "mute" in command:
                pyautogui.press("volumemute")
            return True
        except Exception as e:
            print(f"Volume control error: {e}")
            return False

    def _adjust_brightness(self, command: str) -> bool:
        if platform.system() == "Windows":
            level = "100" if "up" in command else "30"
            try:
                subprocess.run([
                    "powershell",
                    f"(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{level})"
                ], shell=True)
                return True
            except Exception as e:
                print(f"Brightness error: {e}")
                return False
        return False
