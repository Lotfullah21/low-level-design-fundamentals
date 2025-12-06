from abc import ABC, abstractmethod

class Bird(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()

    def fly(self):
        print(f"{self.name} is flying... ...")

    def make_sound(self):
        print(f"{self.name} is making sound")

class SwimmingBird(Bird):
    def move(self):
        self.swim()
    
    def swim(self):
        print(f"{self.name} is swimming")
    
    def make_sound(self):
        print(f"{self.name} is making sound")
    
class FlylessBird(Bird):
    def move(self):
        self.walk()
    
    def walk(self):
        print(f"{self.name} is walking.....")
    
    def make_sound(self):
        print(f"{self.name} is making sound")

eagle = FlyingBird("Eagle")
eagle.fly()
eagle.move()



