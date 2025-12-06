from abc import ABC, abstractmethod

class Vehicle(ABC):   
    def __init__(self, name) -> None:
        self.name = name
    @abstractmethod
    def move(self):
        pass
        
class FuelVehicle(Vehicle):
    @abstractmethod
    def fill(self):
        pass


class Car(FuelVehicle):
    def fill(self):
        self.fill_gas()
    
    def fill_gas(self):
        print("Filling the gas....")
    
    def move(self):
        print("Car moving fast...")

        
class Airplane(FuelVehicle):
    def fill(self):
        self.fill_fuel_tank()
    
    def fill_fuel_tank(self):
        print("Filling the tank for airplane...")
    
    def move(self):
       self.fly()

    def fly(self):
        print("The airplane is flying...")


class Bicycle(Vehicle):

    def move(self):
        print("Bicycle is moving...")

car = Car("Range Rover")
car.fill()
car.move()
etihad = Airplane("Etihad")
etihad.fill()
etihad.move()


byc = Bicycle("Richards")
byc.move()