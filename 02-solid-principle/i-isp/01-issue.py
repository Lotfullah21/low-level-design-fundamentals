from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def charge_battery(self):
        pass
    
    @abstractmethod
    def fill_fuel_tank(self):
        pass

    @abstractmethod
    def fill_gas(self):
        pass

    @abstractmethod
    def fly(self):
        pass
        
class Car(Vehicle):
    
    def charge_battery(self):
        print("Charging the battery...")

    def fill_gas(self):
        print("Filling the gas...")

    def fill_fuel_tank(self):
        print("Filling the tank...")
    
    def fly(self):
        raise Exception("A car cannot fly!")

car = Car()
car.charge_battery()
car.fly()
