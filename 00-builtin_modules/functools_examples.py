
# ----------caching functions----------

from functools import lru_cache

@lru_cache(maxsize=2)
def add_one(a):
    print("calculating")
    return a + 1 

print(add_one(0))
print(add_one(0))
print(add_one(1))
print(add_one(1))


# ----------create partial functions----------

from functools import partial

def add(a, b):
    return a + b

add_one = partial(add, b = 1)

print(add_one(3))


# ----------reduce----------
from functools import reduce

items = ["a","b","c","d","e"]
# add all elements reduce to single element
def add_items(element1, element2):
    return element1 + element2
l = reduce(add_items, items)


# ----------wraps----------
from functools import wraps
# @wraps(func) if used for preserve original function name and doc string while using stacked decorators

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_instance = func(*args, **kwargs)
        return func_instance
    return wrapper

@decorator
def a_function():
    """doc"""
    print("hi")

print(a_function.__name__)



# ----------singledispatch----------

# singledispatch is for creating generic functions for different data types

# regular way
def append_one_old(obj):
    if type(obj) == list:
        return obj + [1]
    elif type(obj) == set:
        return obj.union({1})
    elif type(obj) == str:
        return obj + str(1)
    else:
        print("Unsupported type")
        return obj

# singledispatch way
from functools import singledispatch

@singledispatch
def append_one(obj):
    print("Unsupported type")
    return obj

@append_one.register
def _(obj: list):
    return obj + [1]

@append_one.register
def _(obj: set):
    return obj.union({1})

@append_one.register
def _(obj: str):
    return obj + str(1)

append_one([1,2,3])
append_one({1,2,3})
append_one("abcde")
