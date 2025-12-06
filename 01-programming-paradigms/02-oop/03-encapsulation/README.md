## Encapsulation

Encapsulation means:

- Bundling data (attributes) and methods together in a class (Hold everything together for an entity)
- Restricting direct access to some of the object's components (Protect the entity from outside environment)
- Controlling how data is accessed and modified

## Why Encapsulation?

Without Encapsulation (Bad)

```py
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account = BankAccount("Ahmad", 1000)

# anyone can modify balance directly
# negative balance? No validation!
account.balance = -5000
print(account.balance) # -5000
```

`Problem`: No control over data, anyone can set invalid values.

## Access Modifiers in Python

Python uses **naming conventions** (not strict enforcement) to indicate access levels:

| Convention | Meaning                                  | Example          |
| ---------- | ---------------------------------------- | ---------------- |
| `name`     | Public — accessible everywhere           | `self.name`      |
| `_name`    | Protected — "internal use" by convention | `self._price`    |
| `__name`   | Private — name mangling is applied       | `self.__balance` |

## 1. Public Attributes (No Restriction)

```py
class Course:
    def __init__(self, name, duration):
        self.name = name          # Public
        self.duration = duration  # Public
course = Course("Python", "8 weeks")
# Can access and modify freely
print(course.name)      # Python
course.name = "Java"    # No restriction
print(course.name)      # Java
```

### 2. Protected Attributes (Single Underscore `_`)

Convention only - Python doesn't enforce it, but tells developers "don't access this directly".
Single underscore is just a hint to developers - Python doesn't prevent access.

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self._price = price  # Protected (by convention)

    def get_price(self):
        return self._price

    def apply_discount(self, percentage):
        self._price -= self._price * (percentage / 100)

course = Course("Python", 100)

# technically accessible, but convention says "don't do this"
print(course._price)  # 100 (works, but violates convention)

# Better way
print(course.get_price())  # 100
course.apply_discount(20)
print(course.get_price())  # 80
```

### 3. Private Attributes (Double Underscore \_\_)

Python applies name mangling - makes it harder to access from outside.

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  # Private

    def get_price(self):
        return self.__price

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive")

course = Course("Python", 100)

# Can't access directly
print(course.__price)  # AttributeError: 'Course' object has no attribute '__price'

# Must use methods
print(course.get_price())  # 100
course.set_price(150)
print(course.get_price())  # 150

course.set_price(-50)  # Price must be positive (validation works!)
```

### How Private Attributes Work (Name Mangling)

Python renames `__attribute` to `_ClassName__attribute`:

````py
class Course:
    def __init__(self, name):
        self.name = name
        self.__secret = "Hidden"

course = Course("Python")

# Direct access fails
print(course.__secret)  # AttributeError

# But it's actually stored as _Course__secret
print(course._Course__secret)  # Hidden (works, but don't do this!)

# Check internal attributes
print(course.__dict__)
# {'name': 'Python', '_Course__secret': 'Hidden'}```
````

Important: Private attributes aren't truly private in Python, but name mangling makes accidental access difficult.

### Why Use Encapsulation?

### 1. Data Protection

```py
class BankAccount:
    def __init__(self, balance):
        # protected from direct modification
        self.__balance = balance

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

account = BankAccount(1000)
# account.__balance = -5000 # Wrong
```

### 2. Validation

```py
class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        # validate
        if 0 < age < 120:
            self.__age = age
        else:
            print("Invalid age")

student = Student("Alice", 20)
student.set_age(25)   # Valid
student.set_age(200)  # Invalid age
```

### 3. Flexibility to Change Implementation

```py
class Course:
    def __init__(self, name, hours):
        self.__name = name
        # store in hours
        self.__hours = hours

    def get_duration_weeks(self):
        # convert hours to weeks internally
        return self.__hours // 40

course = Course("Python", 80)
print(course.get_duration_weeks())  # 2
# later, you can change how duration is stored without breaking code
```

## Encapsulation Best Practices

#### 1. Do

```py
class Course:
    def __init__(self, name, price):
        # public - OK to access directly
        self.name = name
        # private - use methods
        self.__price = price

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price > 0:
            self.__price = price
```

#### 2. `

```py
class Course:
    def __init__(self, name, price):
        # don't make everything private
        self.__name = name
        self.__price = price

    # now need getters/setters for everything (tedious)
    def get_name(self):
        return self.__name
```

### Rule of thumb:

- Make attributes public if they don't need validation
- Make attributes private if they need validation or protection
- Use protected `(_)` for internal attributes that subclasses might need

## Summary

| Access Level | Syntax        | Access          | Use Case                                   |
| ------------ | ------------- | --------------- | ------------------------------------------ |
| Public       | `self.name`   | Anywhere        | Simple attributes, no validation needed    |
| Protected    | `self._name`  | Convention only | Internal use, subclass access              |
| Private      | `self.__name` | Name mangled    | Sensitive data, requires controlled access |

#### Encapsulation = Data hiding + Controlled access through methods
