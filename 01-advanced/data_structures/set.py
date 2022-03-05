from typing import FrozenSet


letters = set("cake is a lie")
print(letters)

vowels = {"a", "e", "i", "o", "u"}

intersecs = letters.intersection(vowels)

print(intersecs)

# to create empty set use this
empty = set()

#  this creates empty dict
empty = {}


# non dynamic set
vowels = frozenset({"a", "e", "i", "o", "u"})
print(vowels)


