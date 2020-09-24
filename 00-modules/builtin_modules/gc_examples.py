import gc

# garbage collector

gc.disable()
gc.enable()


for i in range(10):
    l = []
    l.append(l)

# return collected object count
collected = gc.collect()
print(collected)




