import pyautogui
import pyperclip
import time

# Click Chrome
pyautogui.click(1639, 1412)
time.sleep(10)

# Select text
pyautogui.moveTo(992, 207)
pyautogui.dragTo(2208, 1286, duration=1, button="left")

# Copy (macOS)
pyautogui.hotkey("command", "c")

time.sleep(3)

text = pyperclip.paste()

print(text)