Here is the comprehensive summary in a single Markdown file format, without any icons or emojis.

# SOLID Principles in Python

A practical guide to writing clean, maintainable, and scalable Python code using the SOLID design principles introduced by Robert C. Martin.

## Table of Contents

1. Single Responsibility Principle (SRP)
2. Open/Closed Principle (OCP)
3. Liskov Substitution Principle (LSP)
4. Interface Segregation Principle (ISP)
5. Dependency Inversion Principle (DIP)

---

## 1. Single Responsibility Principle (SRP)

**"A class should have only one reason to change."**

Each class should handle exactly one specific job. If a class handles data storage, email notifications, and logging simultaneously, it violates this principle.

### The Violation

In this example, the `User` class is handling both business logic (holding data) and infrastructure logic (sending emails). If the email service changes, the `User` class must change.

```python
class User:
    def __init__(self, name):
        self.name = name

    def register(self):
        print(f"User {self.name} saved to database.")
        # SRP Violation: The User class should not handle email logic.
        print(f"Sending welcome email to {self.name}...")
```

### The Solution

Split the responsibilities into different classes. The `User` class holds data, the `Repository` handles the database, and the `EmailService` handles notifications.

```python
class User:
    def __init__(self, name):
        self.name = name

class UserRepository:
    def save(self, user):
        print(f"User {user.name} saved to database.")

class EmailService:
    def send_welcome_email(self, user):
        print(f"Sending welcome email to {user.name}...")

# The Coordinator
class UserRegistration:
    def register(self, user):
        db = UserRepository()
        email = EmailService()

        db.save(user)
        email.send_welcome_email(user)
```

---

## 2. Open/Closed Principle (OCP)

**"Software entities should be open for extension, but closed for modification."**

You should be able to add new functionality without rewriting existing code. This is usually achieved using inheritance or interfaces.

### The Violation

If we want to add a "Super VIP" discount, we are forced to modify the `calculate` method and add more `if/else` statements. This increases the risk of bugs.

```python
class Discount:
    def calculate(self, price, type):
        if type == "standard":
            return price
        elif type == "vip":
            return price * 0.8
        # We have to keep modifying this method for every new type
```

### The Solution

Use polymorphism. To add a new discount, create a new class that extends the base class. The existing code remains untouched.

```python
from abc import ABC, abstractmethod

class Discount(ABC):
    @abstractmethod
    def calculate(self, price): pass

class StandardDiscount(Discount):
    def calculate(self, price):
        return price

class VIPDiscount(Discount):
    def calculate(self, price):
        return price * 0.8

class SuperVIPDiscount(Discount):
    def calculate(self, price):
        return price * 0.6

# Usage
def get_total(price, discount_strategy: Discount):
    return discount_strategy.calculate(price)
```

---

## 3. Liskov Substitution Principle (LSP)

**"Subtypes must be substitutable for their base types."**

If `Class B` inherits from `Class A`, using `Class B` instead of `Class A` should not crash the program or produce incorrect results.

### The Violation

A Penguin is technically a bird, but it cannot fly. If code expects a `Bird` to be able to `fly()`, passing a Penguin will cause a crash.

```python
class Bird:
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def fly(self):
        raise Exception("I cannot fly!") # Violation

def make_bird_fly(bird: Bird):
    bird.fly() # This will crash if passed a Penguin
```

### The Solution

Refactor the hierarchy based on capabilities (behaviors) rather than strict biological definitions.

```python
class Bird:
    def move(self):
        print("Moving...")

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Penguin(Bird):
    def move(self):
        print("Swimming...")

class Eagle(FlyingBird):
    pass

# Now we can ask specifically for a FlyingBird
def make_bird_fly(bird: FlyingBird):
    bird.fly()
```

---

## 4. Interface Segregation Principle (ISP)

**"Clients should not be forced to depend on interfaces they do not use."**

Avoid "Fat Interfaces" (interfaces with too many methods). It is better to have many small, specific interfaces than one giant, general-purpose one.

### The Violation

The `Worker` interface forces the `Robot` class to implement an `eat` method, which it does not need.

```python
from abc import ABC, abstractmethod

class Worker(ABC):
    @abstractmethod
    def work(self): pass

    @abstractmethod
    def eat(self): pass

class Robot(Worker):
    def work(self):
        print("Robot working...")

    def eat(self):
        # Violation: Robots don't eat, but are forced to implement this.
        raise NotImplementedError()
```

### The Solution

Segregate the interfaces into smaller specific parts.

```python
class Workable(ABC):
    @abstractmethod
    def work(self): pass

class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Human(Workable, Eatable):
    def work(self): print("Human working...")
    def eat(self): print("Human eating...")

class Robot(Workable):
    def work(self): print("Robot working...")
    # Robot is no longer forced to implement 'eat'
```

---

## 5. Dependency Inversion Principle (DIP)

**"High-level modules should not depend on low-level modules. Both should depend on abstractions."**

High-level business logic should not be tightly coupled to low-level tools (like databases, web APIs, or file systems).

### The Violation (Tight Coupling)

The `App` class creates the `MySQLDatabase` instance internally. The App is now "soldered" to MySQL. You cannot switch to PostgreSQL without rewriting the `App` class.

```python
class MySQLDatabase:
    def connect(self):
        return "Connected to MySQL"

class App:
    def __init__(self):
        # Violation: Hard dependency created inside the class.
        self.db = MySQLDatabase()
```

### The Solution (Dependency Injection)

The `App` depends on an abstract `Database` interface. The specific database is passed in (injected) when the App is initialized.

```python
# 1. The Interface (Abstraction)
class Database(ABC):
    @abstractmethod
    def connect(self): pass

# 2. Low Level Modules (Details)
class MySQLDatabase(Database):
    def connect(self): return "MySQL"

class PostgresDatabase(Database):
    def connect(self): return "Postgres"

# 3. High Level Module (Business Logic)
class App:
    def __init__(self, db: Database):
        # The App doesn't care which DB it is, as long as it fits the interface.
        self.db = db

    def start(self):
        print(f"App started with: {self.db.connect()}")

# 4. Usage
mysql = MySQLDatabase()
app = App(mysql) # Plug in MySQL
app.start()
```

## Summary

| Principle                 | Acronym | Main Goal                                                            |
| :------------------------ | :-----: | :------------------------------------------------------------------- |
| **Single Responsibility** |   SRP   | A class should do one thing and do it well.                          |
| **Open/Closed**           |   OCP   | Add new features by creating new classes, not changing old ones.     |
| **Liskov Substitution**   |   LSP   | Subclasses should behave like their parents without breaking things. |
| **Interface Segregation** |   ISP   | Don't force a class to implement methods it doesn't use.             |
| **Dependency Inversion**  |   DIP   | Depend on interfaces (abstractions), not concrete classes.           |
