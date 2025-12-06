from abc import ABC, abstractmethod

# Abstract class No. 1
class Movable(ABC):   
    def __init__(self, name) -> None:
        self.name = name
    @abstractmethod
    def move(self):
        pass

# Abstract class No. 2
class FuelVehicle(ABC):
    def __init__(self, name):
        self.name = name
    @abstractmethod
    def fill(self):
        pass

# Concrete Implementation
class Car(Movable, FuelVehicle):
    def fill(self):
        self.fill_gas()
    
    def fill_gas(self):
        print("Filling the gas....")
    
    def move(self):
        print("Car moving fast...")

# Concrete Implementation  
class Airplane(FuelVehicle, Movable):

    def fill(self):
        self.fill_fuel_tank()
    
    def fill_fuel_tank(self):
        print("Filling the tank for airplane...")
    
    def move(self):
       self.fly()

    def fly(self):
        print("The airplane is flying...")


# Concrete Implementation
class Bicycle(Movable):
    
    def move(self):
        print("Bicycle is moving...")