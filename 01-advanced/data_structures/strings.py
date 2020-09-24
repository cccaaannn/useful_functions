my_str = "can kurt  \na"
my_str2 = "can\nkurt"

# reverse str
my_str[::-1]

# split by space
my_str.split(" ")

# strip strips \n
my_str2.strip()


# string alignment

print("{:<30}".format('left aligned'))
print("{:>30}".format('right aligned'))
print("{:^30}".format('centered'))
print("{:*^30}".format('centered'))


# string formatting

name = "can"
value = 2

# old way
print("name is %s value is %s" % (name, value))
print("name is %(n)s value is %(v)s" % {'n': name, 'v': value})

# format string
print("name is {} value is {}".format(name, value))
print("name is {0} value is {1}".format(name, value))
print("name is {n} value is {v}".format(n=name, v=value))

# f-string formatting in Python 3.6
print(f'name is {name} value is {value}')


inner = f"fsting {value}"
print(f'you can use {f"nested {inner}"}')


# float formatting

float_number = 4863.4343091  

# round ing with a precision
print(f"{float_number:.6}")
print("{0:.6}".format(float_number))

# cutting from a point
print("{0:.4f}".format(float_number))

# adding seperators to numbers
print("{0:,.4f}".format(float_number))
print("{0:_.4f}".format(float_number))


# converting to percentage automatically
questions = 50
correct_answers = 10
print(f"{correct_answers / questions :.2%}")

