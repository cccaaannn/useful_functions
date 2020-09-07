import winsound

# frequency Hz 
frequency = 500
# duration milliseconds              
duration = 1000

winsound.Beep(frequency, duration)

# plays wav 
winsound.PlaySound("sample.wav", winsound.SND_ASYNC)
