'''Abstraction hides the complexity of the system by exposing only the relevant details. 
In Python, we achieve abstraction using abstract base classes (ABCs) from the `abc` module.

python'''


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car starts."

class Bike(Vehicle):
    def start(self):
        return "Bike starts."

car = Car()
bike = Bike()
print(car.start())  # Output: Car starts.
print(bike.start())  # Output: Bike starts.

