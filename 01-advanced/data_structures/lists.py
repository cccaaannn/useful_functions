items = [1,2,3,1,1,4,2,1]
items2 = [1,2,3,1,1,4,2,1]

# reverse list
items[::-1]


# hard copy a list
a = [1,2,3]
b = a # shallow copy
b = a[:] # hard copy


# most_frequent_item
most_frequent_item = max(set(items),key=items.count)

# remove duplicates
list(set(items))

# count elements of a list
from collections import Counter
Counter(items)

# make the list immutable
items2 = frozenset(items2)

