import traceback

try:
    raise Exception("some exception")
except Exception as e:
    print("hi")
    # print(e) # don't do that
    t = traceback.format_exc() # thats better
    print(t)
