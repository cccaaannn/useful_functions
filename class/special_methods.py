
class employee:

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + "." + last + "@email.com"
        self.salary = salary

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # for debuging or logging (mostly for developers)
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.salary)

    # more readable form of __repr__ (to string)
    def __str__(self):
        return "{} - {}".format(self.fullname(), self.email)


    # + operator overloading
    def __add__(self, other):
        return self.salary + other.pay

    # used when len() is called
    def __len__(self):
        return len(self.fullname())


e1 = employee("test", "testsurname", 1000)
e2 = employee("test2", "testsurname2", 2000)


print(e1)
print(repr(e1))
print(len(e1))
print(e1+e2)

