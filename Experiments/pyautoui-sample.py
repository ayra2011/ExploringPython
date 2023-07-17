import pyautogui
import time
import sys
from datetime import datetime
pyautogui.FAILSAFE = False
sleep_interval = 8
start_row = 170
end_row = 1000
start_col = 1630
column_decrement_size = 130
row_increment_size = 50
row: int = start_row
column: int = start_col
while True:
    time.sleep(sleep_interval)
    pyautogui.moveTo(column, row)
    pyautogui.click()
    time.sleep(sleep_interval)
    row += row_increment_size
    if row >= end_row:
        row = start_row
        column -= column_decrement_size
    if column <= (start_col - (4 * column_decrement_size)):
        column = start_col

    # pyautogui.moveTo(1, 1)

# for i in range(0, 3):
#     pyautogui.press("shift")
# print(f"Movement made at {datetime.now().time()}")
