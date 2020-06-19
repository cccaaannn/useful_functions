dict1 = {'One':1, 'Two':2}
dict2 = {'Two':2, 'Three':3}
list1 = ["One","Two","Three"]
list2 = [1,2,3]

# merge 2 dicts
dictionary = {**dict1, **dict2}

# 2 lists to dict
d = dict(zip(list1, list2))
