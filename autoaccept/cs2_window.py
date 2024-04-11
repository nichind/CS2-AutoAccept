import time
import win32gui
from mss import mss
from PIL import Image
import cv2
import numpy as np
import pyautogui


class Window:
    def __init__(self):
        self.found_windows = {}
        self.cs2 = False

    def refresh_windows(self):
        found_windows = {}

        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                rect = win32gui.GetWindowRect(hwnd)
                w = rect[2] - rect[0]
                h = rect[3] - rect[1]
                found_windows[str(hwnd)] = {"name": str(win32gui.GetWindowText(hwnd)), "w": w, "h": h, "x": rect[0],
                                            "y": rect[1]}

        win32gui.EnumWindows(win_enum_handler, None)

        for window in found_windows:
            if found_windows[window]["name"] == 'Counter-Strike 2':
                self.cs2 = True
                print(f'CS2 found, hwnd: {window}')

                self.found_windows = found_windows
                self.window_hwnd = window

                self.window_hwnd = str(self.window_hwnd)
                self.balance = 0

                break

            self.cs2 = False

        def win_enum_handler(hwnd, ctx):
            if win32gui.IsWindowVisible(hwnd):
                rect = win32gui.GetWindowRect(hwnd)
                w = rect[2] - rect[0]
                h = rect[3] - rect[1]
                found_windows[str(hwnd)] = {"name": str(win32gui.GetWindowText(hwnd)), "w": w, "h": h, "x": rect[0], "y": rect[1]}

        win32gui.EnumWindows(win_enum_handler, None)
        self.found_windows = found_windows

    def get_window(self):
        """"""
        while True:
            self.refresh_windows()
            if self.cs2:
                ss = Image.open(mss().shot(output='./buf.jpg'))
                cropped = ss.crop((self.found_windows[self.window_hwnd]['x'] + (self.found_windows[self.window_hwnd]['w'] // 2.5),
                                   self.found_windows[self.window_hwnd]['y'] + (self.found_windows[self.window_hwnd]['h'] // 2.7),
                                   self.found_windows[self.window_hwnd]['x'] + (self.found_windows[self.window_hwnd]['w'] // 1.8),
                                   self.found_windows[self.window_hwnd]['y'] + (self.found_windows[self.window_hwnd]['h'] // 1.7)))
                cropped.save(f'./buf.jpg')
                img = cv2.imread(f'./buf.jpg')
                lower_val = np.array([37, 42, 0])
                upper_val = np.array([84, 255, 255])

                hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
                mask = cv2.inRange(hsv, lower_val, upper_val)

                if np.sum(mask) > 5000000:
                    print(f'Accept button found..? Trying to accept.')
                    pyautogui.click(self.found_windows[self.window_hwnd]['x'] + (self.found_windows[self.window_hwnd]['w'] // 2),
                                     self.found_windows[self.window_hwnd]['y'] + (self.found_windows[self.window_hwnd]['h'] // 2) - 90)
            else:
                print(f'CS2 Window not found, waiting...')
            time.sleep(7)
