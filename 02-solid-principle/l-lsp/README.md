## L - Liskov Substitution Principle (LSP)

##### Definition:

Objects of a superclass should be replaceable with objects of a subclass without breaking the application.

#### In simple terms:

- If you have a parent class and a child class
- You should be able to use the child class wherever you use the parent class
- Without any surprises, errors, or unexpected behavior

`The Liskov Test`: "Can I substitute a child object for a parent object and everything still works correctly?"

#### Why LSP Matters

1. Ensures Correct Inheritance

- Prevents misuse of inheritance
- Child classes truly "are-a" parent class
- No broken hierarchies

2. Safe Polymorphism

- Can rely on parent class interface
- No runtime surprises
- Predictable behavior

3. Prevents Bugs

- No unexpected exceptions from subclasses
- Consistent contracts across hierarchy
- Reliable code

4. Better Design

- Forces you to think about relationships
- Leads to better abstractions
- More maintainable code

```py
from abc import ABC, abstractmethod

class Bird(ABC):
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
    def fly(self):
        print("Penguin cannot fly")
    def make_sound(self):
        print("Penguin is making sound")

eagle = Eagle()
penguin = Penguin()
penguin.fly()
eagle.fly()
```

## Solution:

#### LSP is satisfied!

- Can substitute FlyingBird, SwimmingBird, or FlightlessBird for Bird
- No exceptions, no broken contracts
- Proper abstraction hierarchy

####

```py
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

class FlightlessBird(Bird):
    def move(self):
        self.walk()

    def walk(self):
        print(f"{self.name} is walking.....")

    def make_sound(self):
        print(f"{self.name} is making sound")

eagle = FlyingBird("Eagle")
eagle.fly()
eagle.move()
```

### What LSP Says About This:

LSP doesn't specifically say whether to create concrete classes or instantiate directly. BUT it cares about:

- `Substitutability`: Above code satisfies this
- `Proper abstraction levels`: This needs improvement

```py
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

# 2. Abstract categories (still can't instantiate)
class FlyingBird(Bird):
    def move(self):
        self.fly()

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


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
        print(f"{self.name} soars high with powerful wings! 🦅")

    def make_sound(self):
        print(f"{self.name} screeches: SCREECH! 🦅")


class Sparrow(FlyingBird):
    """Different concrete implementation"""
    def fly(self):
        print(f"{self.name} flutters quickly through trees! 🐦")

    def make_sound(self):
        print(f"{self.name} chirps: Chirp chirp! 🐦")


class Penguin(FlightlessBird):
    """Concrete flightless bird"""
    def walk(self):
        print(f"{self.name} waddles on ice! 🐧")

    def make_sound(self):
        print(f"{self.name} honks: HONK HONK! 🐧")


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
```

## Why Concrete Classes Are Better

### 1. **Proper Abstraction Hierarchy**

```
Bird (abstract)
├── FlyingBird (abstract category)
│   ├── Eagle (concrete)
│   ├── Sparrow (concrete)
│   └── Hawk (concrete)
├── FlightlessBird (abstract category)
│   ├── Penguin (concrete)
│   ├── Ostrich (concrete)
│   └── Kiwi (concrete)
└── SwimmingBird (abstract category)
    ├── Duck (concrete)
    └── Swan (concrete)

```

```py
# Layer 1: Base abstraction (abstract)
class Bird(ABC):
    pass

# Layer 2: Category abstraction (abstract)
class FlyingBird(Bird):
    @abstractmethod
    def fly(self):
        pass

# Layer 3: Concrete implementation (instantiable)
class Eagle(FlyingBird):
    def fly(self):
        # Concrete implementation
        pass

# Instantiate only Layer 3!
eagle = Eagle("Baldy")
```

### The Test:

```py
birds: List[Bird] = [
    FlyingBird("Eagle"),
    FlightlessBird("Penguin"),
    SwimmingBird("Duck")
]

for bird in birds:
    bird.move()        # Works for all!
    bird.make_sound()  # Works for all!
```

The code passes LSP because:

- All children implement move() and make_sound()
- No exceptions thrown
- No broken behavior
- Can substitute any child for Bird

### Best Practice: The Rule

Classes should be either abstract (can't instantiate) or concrete (fully implemented), not in-between.
