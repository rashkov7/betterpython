"""
Encapsulation is the practice of keeping the internal
details of an object hidden from the outside world and providing a simplified interface
for interacting with the object.
"""


# TODO Encapsulation


class Person:

    def __init__(self, name, gender, age):
        self.__age = age
        self.name = name
        self.gender = gender

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value > 18:
            self.__age = value
        else:
            print('Not allowed !')


man = Person('Joro', 'Man', 34)
man.age = 3
print(man.age)