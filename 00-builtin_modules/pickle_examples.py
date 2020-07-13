import pickle

# pickle can serialize python objects

data = {1:"hi", 2: "there"}

# convert to byte
byte_data = pickle.dumps(data)

# convert back to python object
data2 = pickle.loads(byte_data)


# ----------using with files----------
filename = ""

# write to a file
pickle.dump(data, open(filename, "wb" ))

with open(filename, "wb") as f:
    pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)

# read from file
unpickled_object = pickle.load(open(filename ,"rb"))


