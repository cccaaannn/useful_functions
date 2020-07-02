from functools import wraps
import concurrent.futures
import threading
import time


# with regular threads we cant return a value
def threaded_old(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        thread_instance = threading.Thread(target=func, args=[*args])
        thread_instance.setDaemon(True)
        thread_instance.start()
        return thread_instance
    return wrapper

# ThreadPoolExecutor
def threaded(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        executor = concurrent.futures.ThreadPoolExecutor()
        future = executor.submit(func, *args)
        return future
    return wrapper


@threaded
def do_something(seconds):
    time.sleep(seconds)
    print("done...")
    return "some result"


executer_furute = do_something(1.5)

# ----
# do stuff on main thread
print("hi")
# ----

# get the result
print(executer_furute.result())

