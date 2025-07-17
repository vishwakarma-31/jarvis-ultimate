import os
import subprocess
import pyautogui
import platform

class SystemController:
    def handle(self, command: str) -> bool:
        command = command.lower()
        if "open" in command:
            return self._launch_app(command)
        if "volume" in command:
            return self._adjust_volume(command)
        if "brightness" in command:
            return self._adjust_brightness(command)
        if "shutdown" in command:
            os.system("shutdown /s /t 1")
            return True
        return False

    def _launch_app(self, command):
        apps = {
            "chrome": "chrome",
            "notepad": "notepad",
            "file explorer": "explorer",
            "vs code": "code",
            "calculator": "calc"
        }
        for key, value in apps.items():
            if key in command:
                try:
                    subprocess.Popen(value)
                    return True
                except:
                    return False
        return False

    def _adjust_volume(self, command):
        try:
            if "up" in command:
                pyautogui.press("volumeup")
            elif "down" in command:
                pyautogui.press("volumedown")
            elif "mute" in command:
                pyautogui.press("volumemute")
            return True
        except:
            return False

    def _adjust_brightness(self, command):
        if platform.system() == "Windows":
            level = "80" if "up" in command else "30"
            try:
                subprocess.run([
                    "powershell",
                    "(Get-WmiObject -Namespace root/WMI -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{})".format(level)
                ])
                return True
            except:
                return False
        return False
