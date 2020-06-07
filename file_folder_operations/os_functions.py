import os

# Get current working directory
os.getcwd()

# Change directory
os.chdir("path")

# List directory
os.listdir()

# creating directories
os.mkdir() 
os.makedirs()

# Remove directories
os.rmdir("path")
os.removedirs("path") 

# Rename
os.rename("test.txt", "test2.txt")

# Look at info about files st_size (bytes), st_mtime (time stamp)
os.stat("test.txt")

# Access home directory
os.environ.get("HOME")

# os.walk is a generator that yields a tuple of 3 values as it walks the directory tree
for dirpath, dirnames, filenames in os.walk("routepath"): 
    print("Current Path:", dirpath)
    print("Directories:", dirnames)
    print("Files:", filenames)
    print()


# os.path

# join two files together
os.path.join(os.environ.get("HOME"), "test.txt")

# separate filename
os.path.basename

# returns the directory /tmp
os.path.dirname("/tmp/test.txt")

# returns both the directory and the file as a tuple
os.path.split("/tmp/test.txt")

# is exists
os.path.exists("/tmp/test.txt")

# isdir
os.path.isdir("/tmp/test.txt")

# isfile
os.path.isfile("/tmp/test.txt")

# Splits file route of the path and the extension
os.path.splitext("/tmp/test.txt")
