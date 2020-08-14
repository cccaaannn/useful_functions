# recursive factorial
def factorial(num):
    if(num < 2):
        return 1
    else:
        return num * factorial(num - 1)
# res = factorial(998) # max recursion depth


# print reverse list
l = [0,1,2,3,4,5,6,7,8,9]
def print_reverse_list(l, index):
    if(index > len(l)-1):
        return
    else:
        print_reverse_list(l, index + 1)
        print(l[index])
print_reverse_list(l, 0)

