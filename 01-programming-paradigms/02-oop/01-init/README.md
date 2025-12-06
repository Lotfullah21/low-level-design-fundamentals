# What is object?

object in Python is the root of all classes.

It is the top-level built-in base class that every class ultimately inherits from — even if you don’t write it.

object is:

- The most basic, minimal class in Python
- The parent of all classes
- The class that provides:
  - memory allocation
  - `__new__`
  - `__str__, __repr__`
  - attribute mechanics
  - base behavior for every instance
  - It is at the top of Python’s inheritance hierarchy.

It is at the top of Python’s inheritance hierarchy.

## 1. Class

The class keyword defines a blueprint or template for creating objects.

```py
class Course:
    pass
```

Think of it like an architectural blueprint for a house - it's not the actual house, just the design.

## 2. What is an Instance?

An instance is an actual object created from a class.

```py
class Course:
    pass

# creating instances or real objects from a class
course1 = Course()
course2 = Course()
print(course1)  # <__main__.Course object at 0x7f8b4c3d2e10>
print(course2)  # <__main__.Course object at 0x7f8b4c3d2e50>
# Different memory addresses = different objects
```

```sh
<__main__.Course object at 0x100f1a900>
 ^^^^^^^^ ^^^^^^ ^^^^^^    ^^^^^^^^^^^^
    |       |      |            |
    |       |      |            └─ Memory address (hexadecimal)
    |       |      └─ It's an object
    |       └─ Class name
    └─ Module name (file where class is defined)
```

## 3. The `__init__` Method (Constructor)

`__init__`is a special method that runs automatically when we create a new instance. It initializes (sets up) the object.

Why is it called `__init__`?

`__init__` stands for initialize
The double underscores (`__`) mean it's a special method (also called "dunder" method - double underscore)
It's not a constructor (technically, `**new\_\_` creates the object), but it initializes the newly created object

## 4. What is self?

self refers to the specific instance that is calling the method or the current object we are working with.

### Behind the Scenes

When you call `course1.get_subjects()`, Python automatically does:

- `Course.get_subjects(course1)` # Passes course1 as the first argument
- That's why every instance method must have self as the first parameter - to receive the instance!

## 5. Why Do We Use self?

```py

class Course:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def get_subjects(self):
        # self refers to the current course object, if self is not here, the program does not know which subjects we are referring to
        return self.subjects

    def get_subjects(self):
        # self refers to the current course object, if self is not here, the program does not know which subjects we are referring to
        return self.name

course1 = Course("ML", 12)
course2 = Course("Python", 24)
print(course1.get_subjects()) # ML (self=course1, so self.name=Ml)
print(course2.get_subjects()) # Python (self=course2, so self.name=Python)
```

Without self, how would Python know which course's name to print?

## 6. Can We Use Other Names Instead of self?

Yes, we can use any name, but self is the universal convention.

```py
class Course:
    def __init__(this, name, subjects):
        this.name = name
        this.subjects = subjects

    def get_subjects(this):
        # this refers to the current course object, if this is not here, the program does not know which subjects we are referring to
        return this.subjects
```

Whatever keyword we use in `__init__` method, that should be used for the rest of the code.

```py
class Course:
    def __init__(this, name, subjects):
        this.name = name
        this.subjects = subjects

    def get_subjects(this):
        # Wrong, `this` keyword should be used
        return obj.subjects
```

### 7. Instance Variables vs Local Variables

`Instance Variables (with self)`: Stored in the object, accessible anywhere in the class.

`Local Variables (without self)`: Only exist during the method execution.

```py
class Course:
    def __init__(self, name, subjects):
        self.name = name
        # Instance variable (stored in objects)
        self.subjects = subjects

    def get_subjects(self):
        # Local variable, accessible during the method call only
        desc = "Total subjects = "
        return desc + self.subjects

course1 = Course("ML", 12)
print(course1.get_subjects())
```

| Term                  | Meaning                                             | Example               |
| --------------------- | --------------------------------------------------- | --------------------- |
| **Class**             | Blueprint/template                                  | `class Course:`       |
| **Instance**          | Actual object created from class                    | `course1 = course()`  |
| **`__init__`**        | Initialization method (runs when creating instance) | `def __init__(self):` |
| **`self`**            | Reference to the current instance                   | `self.name = name`    |
| **Instance Variable** | Data stored in the object                           | `self.duration = 12`  |
| **Instance Method**   | Function that operates on the instance              | `def get_name(self):` |
| **Constructor**       | `__init__` method (initializes object)              | Called automatically  |
