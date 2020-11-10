# https://github.com/AndreMiras/pycaw
# pip install pycaw

# Python Core Audio Windows Library, working for both Python2 and Python3.


from pycaw.pycaw import AudioUtilities


def main():
    sessions = AudioUtilities.GetAllSessions()
    for session in sessions:
        volume = session.SimpleAudioVolume
        if(session.Process):
            print(session.Process.name())
        if session.Process and session.Process.name() == "chrome.exe":
            volume.SetMute(0, None)
        else:
            volume.SetMute(1, None)


if __name__ == "__main__":
    main()