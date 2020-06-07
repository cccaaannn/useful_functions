
class employee:

    # static variables
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.salary = salary

        employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        employee.salary = int(self.salary * employee.raise_amt)

    # we can use classmethods to change static variables
    @classmethod
    def set_salary_multiplier(cls, amount):
        cls.raise_amt = amount

    # this works like an alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True



e1 = employee("test", "testsurname", 1000)
e2 = employee("test2", "testsurname2", 2000)

employee.set_salary_multiplier(1.05)
print(employee.raise_amt)




# using classmethod as alternative constructor
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
new_emp_1 = employee.from_string(emp_str_1)


# static method
import datetime
my_date = datetime.date(2016, 7, 11)
print(employee.is_workday(my_date))