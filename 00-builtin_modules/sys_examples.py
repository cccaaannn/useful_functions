import sys

# print to console
sys.stdout.write("hi")

# write error message to console
sys.stderr.write("sa")
sys.stderr.flush()

# get programs parameters
sys.argv

# siz of an object
sys.getsizeof(range(0, 10000))

# get ref count of an object
l = []
l_address = id(l)
sys.getrefcount(l_address)

# exit program
sys.exit()