import time
import pyautogui
import pygetwindow as gw

# Find the window
window = gw.getWindowsWithTitle('Minecraft Dungeons')[0]  # Make sure the window title is correct
window.activate()

# Wait a moment for the window to focus
import os
os.system('.\Module\skin1st.py')

time.sleep(1)


# First command: camerathirdperson
pyautogui.typewrite('` camera firstperson | changesize 1 | fov 120', interval=0.01)

# Press | after the third command
pyautogui.press('enter')

import os
import subprocess
