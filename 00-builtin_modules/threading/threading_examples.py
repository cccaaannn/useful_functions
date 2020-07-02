import threading
import time


def do_something(seconds):
    time.sleep(seconds)
    print("done...")


# simple thread example
t = threading.Thread(target=do_something, args=[1.5])

# start thread
t.start()
# ----
# do stuff on main thread
print("hi")
# ----

# join thread
t.join()



# example with multiple threads

# create 10 threads
threads = []
for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.5])
    threads.append(t)

# start threads
for thread in threads:
    thread.start()
 
# ----
# do stuff on main thread
print("hi")
# ----

# join threads
for thread in threads:
    thread.join()
