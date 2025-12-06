from abc import ABC, abstractmethod

# 1. Abstract base
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

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

# 2. Abstract categories (still can't instantiate)
class FlightlessBird(Bird):
    def move(self):
        self.walk()

    @abstractmethod
    def walk(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class SwimmingBird(Bird):
    def move(self):
        self.swim()

    @abstractmethod
    def swim(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


# 3. CONCRETE classes - these we instantiate
class Eagle(FlyingBird):
    """Concrete implementation"""
    def fly(self):
        print(f"{self.name} soars high with powerful wings!")

    def make_sound(self):
        print(f"{self.name} screeches: SCREECH!")


class Sparrow(FlyingBird):
    """Different concrete implementation"""
    def fly(self):
        print(f"{self.name} flutters quickly through trees!")

    def make_sound(self):
        print(f"{self.name} chirps: Chirp chirp!")


class Penguin(FlightlessBird):
    """Concrete flightless bird"""
    def walk(self):
        print(f"{self.name} waddles on ice!")

    def make_sound(self):
        print(f"{self.name} honks: HONK HONK!")


class Duck(SwimmingBird):
    """Concrete swimming bird"""
    def swim(self):
        print(f"{self.name} paddles in the pond! 🦆")

    def make_sound(self):
        print(f"{self.name} quacks: QUACK QUACK! 🦆")


# Usage - Now with real species!
def demonstrate_birds():
    # Create concrete bird instances
    eagle = Eagle("Baldy")
    sparrow = Sparrow("Tweety")
    penguin = Penguin("Pingu")
    duck = Duck("Donald")

    birds = [eagle, sparrow, penguin, duck]

    print("="*60)
    print("DEMONSTRATING LSP WITH CONCRETE BIRDS")
    print("="*60)

    for bird in birds:
        print(f"\n--- {bird.__class__.__name__}: {bird.name} ---")
        # Polymorphism! Works for all
        bird.move()
        bird.make_sound()

    print("\n" + "="*60)
    print("LSP SATISFIED: All concrete birds are substitutable!")
    print("="*60)
demonstrate_birds()
