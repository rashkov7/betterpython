from abc import ABC, abstractmethod

"""
ABSTRACT method is a method that has declaration but doesn't have an implementation.
"""


# TODO ABSTRACTION


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):

    def start(self):
        print(f'Vehicle start the engine')


car = Car()
car.start()
