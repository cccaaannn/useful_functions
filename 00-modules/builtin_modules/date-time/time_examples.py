import time


# get timestamp
start = time.time()

# get time from timestamp
time.gmtime(0)

# get time
time.localtime()

# format time
time.strftime("%Y/%B/%A")

# delay
time.sleep(1)


# usage example
# execution time
start = time.time()

time.sleep(1)

end = time.time()
total = end - start
print(total)


