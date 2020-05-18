items = ["aa","aaaa","abcd","1234","000000"]
items2 = ["aa","aaaa",11,1111,123,1.5]

# examples
[print(item) for item in items]


# single if in list comprehension
l = [item for item in items2 if isinstance(item, int)]

#  if else in list comprehension
l = [item if isinstance(item, int) else None for item in items2]

# multiple if conditions in list comprehension
l = [item if isinstance(item, int) else ("str" if isinstance(item, str) else None) for item in items2]

