import pyautogui
import numpy as np
from PIL import Image
from playsound import playsound
import cv2

def find_image_on_screen(image_path, threshold=0.8):
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot).astype('float32')

    # Load the image file
    needle = Image.open(image_path)
    needle = np.array(needle).astype('float32')

    # Ensure both images have the same number of dimensions
    if len(screenshot.shape) != len(needle.shape):
        print("The dimensions of the screenshot and the needle image do not match.")
        return []

    # Use template Matching to find the image in the screenshot
    result = cv2.matchTemplate(screenshot, needle, cv2.TM_CCOEFF_NORMED)

    # Get the locations of the image in the screenshot
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    return locations

def play_sound_if_image_found(image_path, sound_path, threshold=0.8):
    locations = find_image_on_screen(image_path, threshold)

    if locations:
        print(f"Image found at: {locations}")
        playsound(sound_path)
    else:
        print("Image not found")

def exit_action(icon, item):
    icon.stop()

# Usage
play_sound_if_image_found('Images/neutral24.bmp', 'Sounds/sonar.wav', threshold=0.8)
