import os
os.chdir('./Module')  # Change directory to ./Module
os.system('Injector.exe --process-name Dungeons-Win64-Shipping.exe --inject unlock.dll')  # Run the command
