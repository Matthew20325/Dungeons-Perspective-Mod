import pygame
import time
import vgamepad as vg
import os
import keyboard
gamepad = vg.VX360Gamepad()
print("Make sure your controller is unplugged and you're on the main screen")
time.sleep(5)
gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
print("Turn your Controller on")
time.sleep(15)
pygame.init()
pygame.joystick.init()
# Initialize pygame and the joystick module
os.system('cls' if os.name == 'nt' else 'clear')
# Initialize the virtual gamepad
print("You Can Now Click A")
# Check if at least one joystick is connected
if pygame.joystick.get_count() == 0:
    print("Turn on your controller")
# Get the first joystick (usually Xbox controller)

joystick = pygame.joystick.Joystick(0)
joystick.init()

import json

class Settings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        """Load settings from a JSON file."""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r') as file:
                self.settings = json.load(file)
        else:
            print("Settings file not found, using default settings.")
            self.settings = {
                'Sensitivity': 24,
            }
            self.save_settings()

    def save_settings(self):
        """Save settings to a JSON file."""
        with open(self.settings_file, 'w') as file:
            json.dump(self.settings, file, indent=4)

    def get(self, key, default=None):
        """Get a setting by key."""
        return self.settings.get(key, default)

    def set(self, key, value):
        """Set a setting."""
        self.settings[key] = value
        self.save_settings()

# Main loop to check the stick state
try:
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Get the state of the left stick (invert Y-axis and set to 0 if negative)
        left_x = joystick.get_axis(0)
        left_y = max(joystick.get_axis(1) * -1, 0)  # Invert Y-axis and set to 0 if negative

        # Get the state of the right stick (no changes applied)
        settings = Settings()

        # Get current settings
        Sensitivity = settings.get('Sensitivity')
        Sensitivity = 100 - Sensitivity

        right_x = joystick.get_axis(2) / Sensitivity
        right_y = joystick.get_axis(3) * -1  # Invert Y-axis without setting to 0

        # Get the state of the buttons
        button_a = joystick.get_button(0)
        button_b = joystick.get_button(1)
        button_x = joystick.get_button(2)
        button_y = joystick.get_button(3)
        left_bumper = joystick.get_button(4)
        right_bumper = joystick.get_button(5)
        back_button = joystick.get_button(6)
        start_button = joystick.get_button(7)
        left_trigger = joystick.get_axis(4)  # Left trigger axis
        right_trigger = joystick.get_axis(5)  # Right trigger axis
        left_thumb_click = keyboard.is_pressed('k')


        # Get the D-pad state (hat switch)
        dpad_x, dpad_y = joystick.get_hat(0)  # (x, y) values range from -1 to 1

        # Swap X-axis values: Use right stick X for left stick X, and keep left stick Y as is
        gamepad.left_joystick_float(right_x, left_y)  # Right stick X for left stick X
        gamepad.right_joystick_float(0, 0)  # Disable the right stick by setting both X and Y to 0

        # Set the button states to pass through
        if button_a:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)

        if button_b:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)

        if button_x:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)

        if button_y:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)

        if left_bumper:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER)

        if right_bumper:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER)

        if back_button:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK)

        if start_button:
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_START)

        # Update the trigger values
        gamepad.left_trigger_float(left_trigger)
        gamepad.right_trigger_float(right_trigger)

        # D-pad handling (using the D-pad as input for the virtual gamepad)
        if dpad_y == 1:  # D-pad up
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP)

        if dpad_y == -1:  # D-pad down
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN)

        if dpad_x == 1:  # D-pad right
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT)

        if dpad_x == -1:  # D-pad left
            gamepad.press_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
        else:
            gamepad.release_button(vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)
                # Get the state of the left thumbstick click


        # Update the gamepad state
        gamepad.update()

        # Wait a bit before checking again
        time.sleep(0.05)

except KeyboardInterrupt:
    print("Exiting...")
    pygame.quit()
