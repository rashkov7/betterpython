"""
Inheritance allows you to create a new class based on an existing class.
The new class inherits all the properties and methods of the existing class and
can also have additional properties and methods of its own.
"""


# TODO Inheritance

class Engine:

    def start_engine(self):
        print('Engine Start')


class Vehicle(Engine):
    type_of_vehicle = None

    def __init__(self, color, type_of_vehicle):
        self.color = color
        self.type_of_vehicle = type_of_vehicle


class ManualTransmission:

    def __init__(self, speed):
        self.speed = speed


class Car(Vehicle, ManualTransmission):

    def __init__(self, color, type_of_vehicle, doors, speed):
        # super().__init__(color, type_of_vehicle)
        ManualTransmission.__init__(self, speed)
        Vehicle.__init__(self, color, type_of_vehicle)

        self.doors = doors


car = Car('Blue', 'BMW', 5, 6)
car.start_engine()
print(car.speed)
