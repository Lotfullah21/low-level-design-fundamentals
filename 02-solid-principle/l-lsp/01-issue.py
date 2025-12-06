from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class Eagle(Bird):
    def fly(self):
        raise Exception("Penguin cannot fly")
    def make_sound(self):
        print("Eagle is making sound")

class Penguin(Bird):
    """
    PROBLEM: Penguins can't fly!
    This violates LSP!
    """
    def fly(self):
        # Option 1: Throw exception - breaks LSP!
        raise Exception(f"{self.name} the penguin can't fly! 🐧")
        
        # Option 2: Do nothing - breaks LSP!
        # print(f"{self.name} waddles instead...")
        
        # Option 3: Return None - breaks LSP!
        # return None
    def make_sound(self):
        print(f"{self.name} is making sound")

eagle = Eagle("Eagle")
penguin = Penguin("Penguin")
penguin.fly()
eagle.fly()