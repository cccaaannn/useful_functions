import concurrent.futures
import time


def do_something(seconds):
    time.sleep(seconds)
    print("done... {0}s".format(seconds))
    return seconds

# run threads with thread pool
with concurrent.futures.ThreadPoolExecutor() as executor:
    result1 = executor.submit(do_something, 2)
    result2 = executor.submit(do_something, 3)

    # getting values as they complate
    for f in concurrent.futures.as_completed([result1, result2]):
        print(f.result())
    
    # or getting at the end
    print(result1.result(), result2.result())


# using map for pools

seconds = [5, 4, 3, 2, 1]

# this done in 15 second 
for sec in seconds:
    do_something(sec)

# same example with thread pool 
# this done in 5 seconds
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = executor.map(do_something, seconds)

