my_str = "can kurt  \na"
my_str2 = "can\nkurt"

# reverse str
my_str[::-1]

# split by space
my_str.split(" ")

# strip strips \n
my_str2.strip()


# left aligned
s = "{:<30}".format('left aligned')

# right aligned
s = "{:>30}".format('right aligned')

# centered
s = "{:^30}".format('centered')

# centered and padded with *
s = "{:*^30}".format('centered')
