import difflib as dl

l1 = ['can', 'caan', 'hi', 'aaa']
l2 = ['can', 'caaan', 'hello', 'aaa']


# finds different items
diff = dl.context_diff(l1, l2)

# for d in diff:
#     print(d)


# finds different letters
diff = dl.ndiff(l1, l2)

# for d in diff:
#     print(d)


# finds close matche can be usefull for typos
diff = dl.get_close_matches("can", l2)

# for d in diff:
#     print(d)




# to make 2 string equal difflib can shows different actions with SequenceMatcher

s1 = "abcde"
s2 = "fabcd"

match = dl.SequenceMatcher(None, s1, s2)
for tag, i1, i2, j1, j2 in match.get_opcodes():
    print("action:", tag)
    print("s1 start {} s1 end {}".format(i1, i2))
    print("s2 start {} s2 end {}".format(j1, j2))
    print()


