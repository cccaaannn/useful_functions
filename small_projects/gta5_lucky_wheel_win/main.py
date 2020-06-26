from pyKey import pressKey, releaseKey
from pynput import keyboard
import time

def on_press(key):
    try:
        k = key.char
    except:
        k = key.name
    if k == "1":
        time.sleep(wait)
        pressKey(key="s")
        releaseKey(key="s")

wait = float(input("wait time:"))

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()