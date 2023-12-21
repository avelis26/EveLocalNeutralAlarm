import cv2
import numpy as np
import os
import pyautogui
import pystray
import sys
import threading
import time
from PIL import Image
from playsound import playsound
from pystray import MenuItem as item

def find_image_on_screen(image_path, threshold=0.8):
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot).astype('float32')
    needle = Image.open(image_path)
    needle = np.array(needle).astype('float32')
    if len(screenshot.shape) != len(needle.shape):
        print("The dimensions of the screenshot and the needle image do not match.")
        return []
    result = cv2.matchTemplate(screenshot, needle, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))
    return locations

def play_sound_if_image_found(image_paths, sound_path, threshold=0.8):
    for image_path in image_paths:
        print(f"Image path: {image_path}")
        try:
            with open(image_path, 'rb') as f:
                print(f"Successfully opened {image_path}")
        except Exception as e:
            print(f"Failed to open {image_path}: {e}")
        while True:
            locations = find_image_on_screen(image_path, threshold)
            if locations:
                playsound(sound_path)
            time.sleep(1)

def exit_action(icon, item):
    icon.stop()
    os._exit(0)

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

icon = Image.open(resource_path('Images/GoonLogo.png'))
icon = pystray.Icon("test_icon", icon, "My System Tray Icon", menu=pystray.Menu(item('Exit', exit_action)))
image_paths = [resource_path('Images/Neutral24BitNormal.bmp'), resource_path('Images/Neutral24BitCompact.bmp')]
sound_path = resource_path('Sounds/sonar.wav')
threading.Thread(target=icon.run).start()
threading.Thread(target=play_sound_if_image_found, args=(image_paths, sound_path, 0.8)).start()
