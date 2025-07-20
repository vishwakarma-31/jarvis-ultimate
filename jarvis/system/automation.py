import pyautogui

class AutomationController:
    def press_hotkey(self, *keys):
        try:
            pyautogui.hotkey(*keys)
            return f"Pressed hotkey: {' + '.join(keys)}"
        except Exception as e:
            return f"Hotkey error: {e}"

    def move_mouse(self, x: int, y: int):
        try:
            pyautogui.moveTo(x, y, duration=0.5)
            return f"Moved mouse to ({x}, {y})"
        except Exception as e:
            return f"Mouse move error: {e}"

    def click_mouse(self, clicks=1):
        try:
            pyautogui.click(clicks=clicks)
            return f"Mouse clicked {clicks} time(s)"
        except Exception as e:
            return f"Mouse click error: {e}"

    def scroll_mouse(self, amount: int):
        try:
            pyautogui.scroll(amount)
            return f"Scrolled {amount}"
        except Exception as e:
            return f"Scroll error: {e}"
