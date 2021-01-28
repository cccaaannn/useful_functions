from pynput import keyboard
import time


def on_activate_h():
    print('<ctrl>+<alt>+h pressed')

def on_activate_i():
    print('<ctrl>+<alt>+i pressed')

mapped_keys = {'<ctrl>+<alt>+h': on_activate_h, '<ctrl>+<alt>+i': on_activate_i}

global_keylistener_thread = keyboard.GlobalHotKeys(mapped_keys)
global_keylistener_thread.start()
# global_keylistener_thread.stop()

time.sleep(10)


