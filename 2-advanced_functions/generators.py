# generators returns iterable generator objects 
# they consume less ram since they generate data when needed

def square_numbers(nums):
    for i in nums:
        yield (i*i)

nums = square_numbers([1,2,3,4,5])
print(next(nums))
print(next(nums))


# like list comprehension but we use ()
nums = (x*x for x in [1,2,3,4,5])
print(next(nums))

