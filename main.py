from autoaccept import Window as CS2
from pynput.keyboard import Key, Listener
import os
import winsound


class Press:
    def __init__(self):
        self.last = ''


press = Press()
def on_press(key):
    if str(key) == "'\\x07'":
        winsound.Beep(300, 200) # don't get scared lol.
        os._exit(1)


if __name__ == '__main__':
    Listener(on_press=on_press).start()
    print('Press CTRL + G to exit.')
    CS2().get_window()
