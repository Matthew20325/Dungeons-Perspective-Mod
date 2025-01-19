import shutil
import os
import pyautogui
import time
import pygetwindow as gw
# Read the destination folder path from the config.txt file
config_file = os.path.join(os.getcwd(), 'config.txt')
window = gw.getWindowsWithTitle('Minecraft Dungeons')[0]  # Make sure the window title is correct
# Check if the config.txt file exists
if not os.path.exists(config_file):
    print("config.txt not found!")
    exit(1)

# Read the destination folder from the config file
with open(config_file, 'r') as file:
    destination_folder = file.read().strip()

# Append the subfolder path to the destination folder
destination_folder = os.path.join(destination_folder, 'Dungeons', 'Content', 'Paks', '~mods', 'skins')

# Define the source folder
source_folder = os.path.join(os.getcwd(), 'Module', 'Assets', 'invisible')

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    print(f"Destination folder '{destination_folder}' does not exist.")
    exit(1)

# Ensure the source folder exists
if not os.path.exists(source_folder):
    print(f"Source folder '{source_folder}' does not exist.")
    exit(1)

# Iterate over files in the source folder
for filename in os.listdir(source_folder):
    source_file = os.path.join(source_folder, filename)
    destination_file = os.path.join(destination_folder, filename)
    
    # If it's a file, copy it to the destination
    if os.path.isfile(source_file):
        shutil.copy(source_file, destination_file)
        print(f"Copied: {filename}")

    else:
        print(f"Skipped (not a file): {filename}")
pyautogui.keyDown('f5')
time.sleep(0.5)
pyautogui.keyUp('f5')
print("Copy operation completed.")