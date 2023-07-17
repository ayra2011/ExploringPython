import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False

x: int = 0
while True:
    time.sleep(5)
    x += 100
    pyautogui.moveTo(1620, x+400)
    pyautogui.click()
    time.sleep(5)
    if x > 1900:
        x = 0
pyautogui.moveTo(1, 1)

# for i in range(0, 3):
#     pyautogui.press("shift")
# print(f"Movement made at {datetime.now().time()}")
