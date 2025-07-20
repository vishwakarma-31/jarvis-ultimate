import pyautogui
import time

class AdvancedAutomation:
    def take_screenshot(self, filename: str = "screenshot.png") -> tuple:
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(filename)
            return f"Screenshot saved as {filename}", True
        except Exception as e:
            return f"Screenshot error: {e}", False


    def get_mouse_position(self) -> str:
        try:
            x, y = pyautogui.position()
            return f"Mouse is at position ({x}, {y})"
        except Exception as e:
            return f"Mouse position error: {e}"

    def type_text(self, text: str):
        try:
            time.sleep(0.5)  # Wait before typing to allow focus
            pyautogui.typewrite(text, interval=0.05)  # Slower typing for reliability
            return f"Typed: {text}", True
        except Exception as e:
            return f"Failed to type: {e}", False

