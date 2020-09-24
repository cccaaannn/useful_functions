class Employee():

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.is_db_connected = False

    def __enter__(self):
        print("entered")
        self.is_db_connected = True

        # must return self because in the with employee as e: e becomes the value returned from __enter__
        return self
    
    def __exit__(self, type, value, traceback):
        print("exited")
        self.is_db_connected = False

    def get_salary(self):
        if(self.is_db_connected):
            print(self.salary)
        else:
            print("db is not connected")



employee = Employee("can", 1000)

employee.get_salary()

with employee as e:
    e.get_salary()


