import winreg

import platform

# get system info to fix 32bit 64bit registry problem
bitness = platform.architecture()[0]
if(bitness == '32bit'):
    other_view_flag = winreg.KEY_WOW64_64KEY
elif(bitness == '64bit'):
    other_view_flag = winreg.KEY_WOW64_32KEY

opened_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, access = (winreg.KEY_READ | other_view_flag))

winreg.DeleteKey(opened_key, "key")
winreg.CreateKey(opened_key, "key")



# raises filenotfound error
try:
    winreg.CreateKey(opened_key, "key")
except FileNotFoundError:
    pass