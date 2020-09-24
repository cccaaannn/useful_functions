import threading
import time

# thread class with kill function
class threader(threading.Thread):
    def __init__(self):
        super().__init__()
        self.is_alive = True

    def kill(self):
        self.is_alive = False

    def run(self):
        while True:
            if(not self.is_alive):
                return

            time.sleep(1)
            print("thread is working")



# run thread for 5 seconds

t = threader()

t.start()

print(t.is_alive)

time.sleep(5)

t.kill()

print(t.is_alive)
