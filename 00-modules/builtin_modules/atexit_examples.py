import atexit

# atexit triggers a function before exit to clean up

def goodbye(number1, number2):
    print("exited", number1, number2)

atexit.register(goodbye, number1=1, number2=2)

# or

@atexit.register
def goodbye():
    print("exited")

