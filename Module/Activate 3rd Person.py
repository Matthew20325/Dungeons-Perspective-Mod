import time
import pyautogui
import pygetwindow as gw

# Find the window
window = gw.getWindowsWithTitle('Minecraft Dungeons')[0]  # Make sure the window title is correct
window.activate()

import os
os.system('.\Module\skin3rd.py')
# Wait a moment for the window to focus
time.sleep(1)

# First command: camerathirdperson
pyautogui.typewrite('` camera thirdperson | changesize 1 | fov 120', interval=0.01)

# Press | after the third command
pyautogui.press('enter')

