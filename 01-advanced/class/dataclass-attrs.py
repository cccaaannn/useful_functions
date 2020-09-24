# after python 3.7 dataclasses are better option
from dataclasses import dataclass

@dataclass
class Car:
    name: str
    price: int
    
car1 = Car("car", 10000)

# __eq__ is implemented on dataclasses
print(car1 == car1)
print(car1.name)
print(car1)




# old approach to create dataclass
# pip install attr
from attr import attrs, attrib

@attrs
class Person(object):
    name = attrib(default='default name')
    surname = attrib(default='default surname')
    age = attrib(init=False)
    
p1 = Person()
p2 = Person('person', 'surname')
p2.age = 60
print(p1)
print(p2)











