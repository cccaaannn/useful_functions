import collections

# counter counts things it is similar to set
# regular name for this datastructure can be also bag or multiset


stuff = collections.Counter()

some_dict = {"can": 1, "not can": 3}
stuff.update(some_dict)

print(stuff)

some_dict2 = {"can": 5, "hi": 2}
stuff.update(some_dict2)

print(stuff)

