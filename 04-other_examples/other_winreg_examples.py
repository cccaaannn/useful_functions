import platform
import winreg

def edit_reg(keys, key_paths, operation="delete"):
    """creates or deletes registry values"""
    # get system info
    bitness = platform.architecture()[0]
    if(bitness == '32bit'):
        other_view_flag = winreg.KEY_WOW64_64KEY
    elif(bitness == '64bit'):
        other_view_flag = winreg.KEY_WOW64_32KEY

    for key in keys:
        for index, key_path in enumerate(key_paths):
            try:
                opened_key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, access = (winreg.KEY_READ | other_view_flag))
                if(operation == "delete"):
                    winreg.DeleteKey(opened_key, keys[key])
                elif(operation == "create"):
                    winreg.CreateKey(opened_key, keys[key])
                else:
                    print("operation {0} is not supported available operations create, delete".format(operation))
                    return
                print("key: {0} - {1} \t found -> {2}".format(key, index+1, operation))
            except FileNotFoundError:
                print("key: {0} - {1} \t not found".format(key, index+1))