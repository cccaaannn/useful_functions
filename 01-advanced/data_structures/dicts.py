dict1 = {'One':1, 'Two':2}
dict2 = {'Two':2, 'Three':3}
list1 = ["One","Two","Three"]
list2 = [1,2,3]

# merge 2 dicts
dictionary = {**dict1, **dict2}

# 2 lists to dict
d = dict(zip(list1, list2))



user_ids = {
    "John": 12,
    "Anna": 2,
    "Jack": 10
}

# bad practice
name = "Paul"

if name in user_ids:
    user_id = user_ids[name]
else:
    user_id = None

# good practice
user_id = user_ids.get(name, None)


# deep copy

import copy

some_dict = {"a":1, "b":2}

shallow_copy = some_dict
shallow_copy2 = some_dict.copy() # this is still a shallow copy eventhough dict address is different addresses of the elements are same.
deep_copy = copy.deepcopy(some_dict)

print(hex(id(some_dict)))
print(hex(id(shallow_copy)))
print(hex(id(shallow_copy2)))
print(hex(id(deep_copy)))