## 1. Abstraction (Hiding Complexity)

Abstraction means hiding the complex implementation details and showing only the essential features.

##### USER DO NOT NEED TO KNOW HOW SOMETHING WORKS, just what it does

## Why Use Abstraction?

- Users don't need to know how something works, just what it does
- Makes code easier to use and maintain
- Provides a clean interface

## Abstract Base Classes (ABC)

Python provides `abc` module to create abstract classes that force child classes to implement certain methods.
`abstractmethod`: It has to be used on top of a method that is required to be implemented by all child classes.

`Key Point`: Abstract classes are like contracts - they say "if you inherit from me, you MUST implement these methods!"

```py
from abc import ABC, abstractmethod
class Course(ABC):

    @abstractmethod
    def get_name(self) ->str:
        """Every course must implement this"""
        pass

    @abstractmethod
    def get_chapters(self) ->str:
        """Every Course must implement this"""
        pass


class Python(Course):
    def __init__(self, name, chapters) -> None:
        self._name = name
        self._chapters = chapters

    def get_name(self):
        return f"{self._name}"

    def get_chapters(self):
        return f"{self._chapters}"

python = Python("Django", 12)
print(python.get_chapters())
print(python.get_name())
```

## 2. Special Methods (Magic Methods / Dunder Methods)

Special methods start and end with double underscores `(__method__)`. They let us customize how objects behave with built-in Python operations.

#### 1. `__str__()` - String Representation for Users

#### 2. `__repr__()` - String Representation for Developers

#### 3. `__len__()` - Make Objects Work with len()

```py
class Python:
    def __init__(self, name, chapters) -> None:
        self.name = name
        self.chapters = chapters

    # def __len__(self):
    #     return self.chapters

python = Python("Django", 12)
print(len(python)) # TypeError: object of type 'Python' has no len()
```

```py
class Python:
    def __init__(self, name, chapters) -> None:
        self.name = name
        self.chapters = chapters

    def __len__(self):
        return self.chapters

python = Python("Django", 12)
print(len(python)) # 12
```

```py
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def __len__(self):
        return len(self.songs)

playlist = Playlist("My Favorites")
playlist.add_song("Song 1")
playlist.add_song("Song 2")

print(len(playlist))  # 2 (calls __len__ behind the scenes!)
```

```py
class Courses:
    def __init__(self):
        self.chapters = []

    def add(self, chapter):
        return self.chapters.append(chapter)

    # makes it indexable
    def __getitem__(self, index):
        return self.chapters[index]

    # Makes 'len' work
    def __len__(self):
        return len(self.chapters)

    # Makes 'in' work
    def __contains__(self, chapter):
        return chapter in self.chapters



courses = Courses()
courses.add("Python")
courses.add("Web Dev")
print(courses.chapters)
print(courses[0])
print(len(courses))
print("Python" in courses)
```

#### Common Special Methods — Cheat Sheet

| Method           | Usage / Trigger          | Example              | Meaning / Purpose        |
| ---------------- | ------------------------ | -------------------- | ------------------------ |
| `__str__()`      | `str(obj)`, `print(obj)` | User-friendly string | Human-readable output    |
| `__repr__()`     | `repr(obj)`              | Developer string     | Unambiguous debug output |
| `__len__()`      | `len(obj)`               | Length of object     | Size/count               |
| `__getitem__()`  | `obj[index]`             | Indexing             | Access by index/key      |
| `__setitem__()`  | `obj[index] = val`       | Set by index         | Assign value             |
| `__contains__()` | `item in obj`            | Membership test      | Check if in collection   |
| `__add__()`      | `obj + other`            | Addition             | Combine/add              |
| `__sub__()`      | `obj - other`            | Subtraction          | Remove/subtract          |
| `__eq__()`       | `obj == other`           | Equality             | Compare equality         |
| `__lt__()`       | `obj < other`            | Less than            | Ordering                 |
| `__gt__()`       | `obj > other`            | Greater than         | Ordering                 |

## Property Decorators (@property)

Properties let us add getters and setters to control how attributes are accessed and modified, while still using simple attribute syntax

#### Why we need them

```py
class Courses:
    def __init__(self, name, price):
        self.name = name
        self.price = price

python = Courses("Python", 10)
print(python.price)
# Wrong approach, how can a price be negative
python.price = -120
print(python.price)
```

#### Syntax

```py
class Courses:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):  # ← This is the GETTER
        return self._price

    @price.setter  # ← This decorator uses the GETTER's name
    def price(self, val):  # ← This is the SETTER
        if val < 0:
            raise ValueError("Price cannot be negative")
        self._price = val
```

##### Step 1: The Getter (@property)

```py
@property
def price(self):  # ← This name "price" is what users will access
    return self._price  # ← Return the private attribute
```

#### What this does:

- Creates a property called price
- When someone writes python.price, it calls this method
- Acts like an attribute, but it's actually a method!

##### Step 2: The Setter (@price.setter)

```py
@price.setter  # ← Must be @{property_name}.setter
# ← Method name must match the property name
def price(self, val):
    if val < 0:
        raise ValueError("Price cannot be negative")
    self._price = val
```

#### What this does:

- When someone writes python.price = 100, it calls this method
- The decorator must be @{property_name}.setter (in this case @price.setter)
- The method name must match the property name (price)

##### Important

- We must have a getter first before we can add a setter.
- The getter name and setter name should match.

```py
@property
def price(self):  # ← This name "price" is what users will access
    return self._price  # ← Return the private attribute
```

#### What this does:

- Creates a property called price
- When someone writes python.price, it calls this method
- Acts like an attribute, but it's actually a method!

##### Step 2: The Setter (@price.setter)

```py
@price.setter  # ← Must be @{property_name}.setter
# ← Method name must match the property name
def price(self, val):
    if val < 0:
        raise ValueError("Price cannot be negative")
    self._price = val
```
