# pip install pyautogui
# https://pyautogui.readthedocs.io/en/latest/

import pyautogui

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size() 
print(screenWidth, screenHeight)


# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position() 
print(currentMouseX, currentMouseY)


# --- mouse ---

# Move the mouse to XY coordinates.
# pyautogui.moveTo(100, 150) 

# Click the mouse.
# pyautogui.click()          

# Move the mouse to XY coordinates and click it.
# pyautogui.click(100, 200) 

# Find where button.png appears on the screen and click it.
# pyautogui.click('button.png') 

# Move mouse 10 pixels down from its current position.
# pyautogui.move(0, 10)      

# Double click the mouse.
# pyautogui.doubleClick()   

# Use tweening/easing function to move mouse over 2 seconds.
# pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad) 


# --- keyboard ---

# type with quarter-second pause in between each key
# pyautogui.write('Hello world!', interval=0.25)  

# Press the Esc key. All key names are in pyautogui.KEY_NAMES
# pyautogui.press('esc')     

# Press the Shift key down and hold it.
# pyautogui.keyDown('shift') 

# Press the left arrow key 4 times.
# pyautogui.press(['left', 'left', 'left', 'left']) 

# Let go of the Shift key.
# pyautogui.keyUp('shift')   

# Press the Ctrl-C hotkey combination.
# pyautogui.hotkey('ctrl', 'c') 

# --- display ---
# Make an alert box appear and pause 
pyautogui.alert('This is the message to display.') 
pyautogui.confirm(text='', title='', buttons=['OK', 'Cancel'])