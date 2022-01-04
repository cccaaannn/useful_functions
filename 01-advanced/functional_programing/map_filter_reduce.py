items = ["aa","aaaa","abcd","1234","000000"]
items2 = ["aa","aaaa",11,1111,123]
items3 = ["a","b","c","d","e"]
items4 = [10,20,30,40,50]



# --------------------map--------------------
# add dash to start, regular function
def add_dash(s):
    return "_" + s
l = list(map(add_dash, items))

# add dash to start, lambda
l = list(map(lambda s: "_" + s, items))



# --------------------filter--------------------
# filter int, regular function
def is_int(element):
    if(isinstance(element, int)):
        return True
    else:
        return False
l = list(filter(is_int, items2))

# filter int, lambda
l = list(filter(lambda element: True if isinstance(element, int) else False, items2))

# list comprehension
l = [item for item in items2 if isinstance(item, int)]

# same filtering with using map and list comprehension
l = [items2[index] for index, mapped_item in enumerate(list(map(lambda element: True if isinstance(element, int) else False, items2))) if mapped_item]


class job:
    def __init__(self, isActive):
        self.isActive = isActive

    def __repr__(self):
        return "job: {}".format(self.isActive)


jobs = [job(1), job(1), job(1), job(0), job(0)]

temp = []
for job in jobs:
    if(job.isActive):
        temp.append(job)
print(temp)

filtered = list(filter(lambda job : job.isActive, jobs))

print(filtered)





# --------------------reduce--------------------
from functools import reduce

# add all elements reduce to single element, regular function
def add_items(element1, element2):
    return element1 + element2
l = reduce(add_items, items3)

# add all elements reduce to single element, lambda 
l = reduce(lambda element1, element2: element1 + element2, items4)


