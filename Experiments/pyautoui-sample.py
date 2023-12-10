import pyautogui
import time
import sys
from datetime import datetime

pyautogui.FAILSAFE = True
# making this true will stop col from changing row clicks will continue to vary, col will be fixed to where mouse is
# found after first 5 seconds
fixed_column: bool = True
scroll_enable: bool = True
vertical_scroll_pixel_count: int = 40
sleep_interval: int = 10
prod_mode: bool = False
if prod_mode:
    sleep_interval = 120
edit_mode: bool = False
# allow time for user to position mouse after running this program at their intended start position  (useful for
# fix_column case)
time.sleep(5)
orig_col, orig_row = pyautogui.position()
print(f"captured orig row: {orig_row}, captured orig column: {orig_col}")

start_row = 160
end_row = 1000
start_col = 1630  # 1430 (general start)

column_decrement_size = 130
row_increment_size = 50
row: int = start_row
column: int = start_col
if fixed_column:  # fix col to start time found col position
    print("")
    column = orig_col
    column_decrement_size = 0
    start_col = orig_col
    count: int = 0
while True:
    time.sleep(sleep_interval)
    orig_col, orig_row = pyautogui.position()
    if scroll_enable:
        count += 1
        if count % 2 == 0:
            pyautogui.scroll(vertical_scroll_pixel_count)
        else:
            pyautogui.scroll(-1 * vertical_scroll_pixel_count)
    pyautogui.moveTo(column, row)
    pyautogui.click()
    print(f"row: {row}, column: {column}")
    pyautogui.moveTo(orig_col, orig_row)
    if edit_mode:
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
