# SOLID Principles

A comprehensive guide to the five fundamental principles of object-oriented design that make software more maintainable, flexible, and scalable.

## Table of Contents

- [What is SOLID?](#what-is-solid)
- [Why SOLID Matters](#why-solid-matters)
- [S - Single Responsibility Principle](#s---single-responsibility-principle)
- [O - Open/Closed Principle](#o---openclosed-principle)
- [L - Liskov Substitution Principle](#l---liskov-substitution-principle)
- [I - Interface Segregation Principle](#i---interface-segregation-principle)
- [D - Dependency Inversion Principle](#d---dependency-inversion-principle)
- [Quick Reference](#quick-reference)

---

## What is SOLID?

SOLID is an acronym for five design principles intended to make software designs more understandable, flexible, and maintainable.

- **S** - Single Responsibility Principle
- **O** - Open/Closed Principle
- **L** - Liskov Substitution Principle
- **I** - Interface Segregation Principle
- **D** - Dependency Inversion Principle

---

## Why SOLID Matters

### Without SOLID

- Code is hard to understand and modify
- Changes break existing functionality
- Testing is difficult
- Code duplication everywhere
- Tight coupling between components

### With SOLID

- Clean, maintainable code
- Easy to extend without breaking existing code
- Simple to test
- Reusable components
- Loose coupling, high cohesion

---

## S - Single Responsibility Principle

### Definition

**A class should have one, and only one, reason to change.**

Each class should do one thing and do it well.

### Bad Example

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_database(self):
        # Database logic
        print(f"Saving {self.name} to database")

    def send_email(self):
        # Email logic
        print(f"Sending email to {self.email}")

    def generate_report(self):
        # Report generation logic
        print(f"Generating report for {self.name}")
```

**Problem:** User class has 3 responsibilities (user data, database, email, reporting). Changes to email or database logic require modifying User class.

### Good Example

```python
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user):
        print(f"Saving {user.name} to database")

class EmailService:
    def send(self, user):
        print(f"Sending email to {user.email}")

class ReportGenerator:
    def generate(self, user):
        print(f"Generating report for {user.name}")

# Usage
user = User("Alice", "alice@example.com")
repo = UserRepository()
email = EmailService()
report = ReportGenerator()

repo.save(user)
email.send(user)
report.generate(user)
```

**Benefits:**

- Each class has one responsibility
- Easy to test each class independently
- Changes are isolated
- Classes are reusable

### Key Points

- One class = one job
- High cohesion within class
- Easy to name the class
- Changes affect minimal code

---

## O - Open/Closed Principle

### Definition

**Software entities should be open for extension but closed for modification.**

Add new functionality by adding new code, not by changing existing code.

### Bad Example

```python
class PaymentProcessor:
    def process(self, amount, payment_type):
        if payment_type == "credit_card":
            print(f"Processing ${amount} via Credit Card")
        elif payment_type == "paypal":
            print(f"Processing ${amount} via PayPal")
        # New requirement - modified existing code!
        elif payment_type == "crypto":
            print(f"Processing ${amount} via Crypto")

# Every new payment method requires modifying this class
processor = PaymentProcessor()
processor.process(100, "credit_card")
processor.process(50, "crypto")
```

**Problem:** Adding new payment methods requires modifying existing code. Risk of breaking existing functionality.

### Good Example

```python
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process(self, amount):
        pass

class CreditCard(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Credit Card")

class PayPal(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via PayPal")
# New class - existing code untouched!
class Crypto(PaymentMethod):
    def process(self, amount):
        print(f"Processing ${amount} via Crypto")

class PaymentProcessor:
    def process_payment(self, amount, method: PaymentMethod):
        method.process(amount)

# Usage
processor = PaymentProcessor()
processor.process_payment(100, CreditCard())
processor.process_payment(50, PayPal())
processor.process_payment(200, Crypto())
```

**Benefits:**

- No modification of existing code
- No risk of breaking working features
- Easy to add new features
- Supports plugin architecture

### Key Points

- Extend behavior through new classes
- Use abstraction (interfaces/abstract classes)
- Existing code remains unchanged
- Apply Strategy pattern

---

## L - Liskov Substitution Principle

### Definition

**Objects of a superclass should be replaceable with objects of a subclass without breaking the application.**

Child classes must be substitutable for their parent classes.

### Bad Example

```python
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flying")

class Penguin(Bird):
    def fly(self):
        # Violates LSP!
        raise Exception("Penguins can't fly!")

def make_bird_fly(bird: Bird):
    bird.fly()

sparrow = Sparrow()
penguin = Penguin()

make_bird_fly(sparrow)
# Crashes! Can't substitute Penguin for Bird
make_bird_fly(penguin)
```

**Problem:** Penguin breaks the contract promised by Bird. Cannot substitute Penguin where Bird is expected.

### Good Example

```python
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        self.fly()

    def fly(self):
        print("Flying in the sky")

class FlightlessBird(Bird):
    def move(self):
        self.walk()

    def walk(self):
        print("Walking on ground")

class Sparrow(FlyingBird):
    def fly(self):
        print("Sparrow flying")

class Penguin(FlightlessBird):
    def walk(self):
        print("Penguin waddling")

def make_bird_move(bird: Bird):
      for all birds
    bird.move()

sparrow = Sparrow()
penguin = Penguin()

make_bird_move(sparrow)
make_bird_move(penguin)
```

**Benefits:**

- All subclasses work correctly as parent
- No unexpected exceptions
- Reliable polymorphism
- Type-safe substitution

### Key Points

- Child must not strengthen preconditions
- Child must not weaken postconditions
- Parent's invariants must be preserved
- No exceptions not in parent

---

## I - Interface Segregation Principle

### Definition

**No client should be forced to depend on methods it does not use.**

Many small, specific interfaces are better than one large, general-purpose interface.

### Bad Example

```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass

class Human(Worker):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

class Robot(Worker):
    def work(self):
        print("Robot working")

    def eat(self):
        # Robot doesn't eat! Forced to implement
        raise NotImplementedError("Robots don't eat")

    def sleep(self):
        # Robot doesn't sleep! Forced to implement
        raise NotImplementedError("Robots don't sleep")

def manage_worker(worker: Worker):
    worker.work()
    # Crashes for Robot!
    worker.eat()
    worker.sleep()

human = Human()
robot = Robot()

manage_worker(human)
manage_worker(robot)
```

**Problem:** Robot forced to implement eat() and sleep() methods it doesn't use.

### Good Example

```python
from abc import ABC, abstractmethod

class Workable(ABC):
    @abstractmethod
    def work(self):
        pass

class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass

class Sleepable(ABC):
    @abstractmethod
    def sleep(self):
        pass

class Human(Workable, Eatable, Sleepable):
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

class Robot(Workable):
    # Only implements what it needs!
    def work(self):
        print("Robot working")

def make_work(worker: Workable):
    worker.work()

def lunch_break(worker: Eatable):
    worker.eat()

def rest_time(worker: Sleepable):
    worker.sleep()

human = Human()
robot = Robot()

make_work(human)
make_work(robot)

lunch_break(human)
# lunch_break(robot) would be a type error - prevented at compile time!

rest_time(human)
# rest_time(robot) would be a type error - prevented at compile time!
```

**Benefits:**

- No forced implementations
- Clients depend only on what they use
- Clear, focused interfaces
- Easy to implement

### Key Points

- Split fat interfaces into smaller ones
- Role-based interfaces
- No empty implementations
- Interface per capability

---

## D - Dependency Inversion Principle

### Definition

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

Depend on interfaces/abstractions, not concrete classes.

### Bad Example

```python
class MySQLDatabase:
    def save(self, data):
        print(f"Saving {data} to MySQL")

class UserService:
    def __init__(self):
        # Direct dependency on concrete class!
        self.db = MySQLDatabase()

    def create_user(self, name):
        self.db.save(name)

# Problem: Locked to MySQL. Can't switch to PostgreSQL without modifying UserService
service = UserService()
service.create_user("Alice")
```

**Problem:** UserService is tightly coupled to MySQLDatabase. Can't swap databases or test easily.

### Good Example

```python
from abc import ABC, abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MySQL")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to PostgreSQL")

class MongoDatabase(Database):
    def save(self, data):
        print(f"Saving {data} to MongoDB")

class UserService:
    # Depends on abstraction!
    def __init__(self, db: Database):
        self.db = db

    def create_user(self, name):
        self.db.save(name)

# Easy to swap implementations
mysql_service = UserService(MySQLDatabase())
mysql_service.create_user("Alice")

postgres_service = UserService(PostgreSQLDatabase())
postgres_service.create_user("Bob")

mongo_service = UserService(MongoDatabase())
mongo_service.create_user("Charlie")
```

**Benefits:**

- Easy to swap implementations
- Easy to test (use mock objects)
- Loose coupling
- Flexible architecture

### Key Points

- Inject dependencies (Dependency Injection)
- Depend on abstractions
- High-level and low-level both depend on interfaces
- Configuration over hard-coding

---

## Quick Reference

### Single Responsibility (SRP)

```python
# One class = one job
class User: pass
class UserRepository: pass
class EmailService: pass
```

### Open/Closed (OCP)

```python
# Extend, don't modify
class PaymentMethod(ABC):
    def process(self): pass

class CreditCard(PaymentMethod): pass
# New class, not modified code
class PayPal(PaymentMethod): pass
```

### Liskov Substitution (LSP)

```python
# Child works wherever parent works
def process(bird: Bird):
    bird.move()   for all Bird subclasses

process(Sparrow())
process(Penguin())   - no exceptions
```

### Interface Segregation (ISP)

```python
# Many small interfaces
class Workable(ABC): pass
class Eatable(ABC): pass

class Human(Workable, Eatable): pass
class Robot(Workable): pass  # Only what it needs
```

### Dependency Inversion (DIP)

```python
# Depend on abstractions
class Service:
     # Abstraction injected
    def __init__(self, db: Database):
        self.db = db

service = Service(MySQLDatabase())
```

---

## SOLID in One Sentence Each

- **S**: One class does one thing
- **O**: Add features by adding code, not changing code
- **L**: Subclass can replace parent without breaking
- **I**: Don't force classes to implement unused methods
- **D**: Inject dependencies, use interfaces

---

## Benefits of Following SOLID

### Maintainability

- Code is easier to understand
- Changes are isolated to specific areas
- Less risk of breaking existing functionality

### Testability

- Easy to write unit tests
- Can mock dependencies
- Test components in isolation

### Flexibility

- Easy to add new features
- Easy to swap implementations
- Support for plugins and extensions

### Scalability

- Code grows without becoming spaghetti
- Team can work on different components
- Clear separation of concerns

---

## Common Anti-Patterns to Avoid

### God Class

A class that does everything. Violates SRP.

### Tight Coupling

Classes directly dependent on concrete implementations. Violates DIP.

### Fragile Base Class

Subclasses break when parent changes. Violates LSP.

### Fat Interface

Interface with too many unrelated methods. Violates ISP.

### Shotgun Surgery

One change requires modifications everywhere. Violates OCP.

---

## When to Apply SOLID

### Always Apply

- SRP: Always have single responsibility
- DIP: Always inject dependencies

### Apply When Needed

- OCP: When you anticipate extensions
- LSP: When using inheritance
- ISP: When interfaces grow large

### Don't Over-Engineer

- Start simple
- Refactor when you see patterns
- Balance SOLID with YAGNI (You Aren't Gonna Need It)

---

## Conclusion

SOLID principles are guidelines, not strict rules. Use them to:

- Write cleaner code
- Make better design decisions
- Create maintainable systems
- Communicate design intent

Practice these principles consistently, and they'll become second nature in your software design process.
