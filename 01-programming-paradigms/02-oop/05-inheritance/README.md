## What is Inheritance?

Inheritance allows a class (child/subclass) to inherit attributes and methods from another class (parent/superclass).

#### Think of it like genetics:

- A child inherits traits from their parents
- The child can have their own unique traits too
- The child can modify inherited traits

<p text-align="center">
    <img src="./assets/inheritance.drawio">
</p>

Considering the above diagram:

- `Every `Mammals` have:
  - all the data and behaviors of an animal
    - Every `Human` have behaviors and data of a `Mammal`

```py
class PythonCourse:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    def set_price(self, price):
        self.price = price
python = PythonCourse("Python", 120)

class MLCourse:
    def __init__(self, name, price):
        # Redundancy, most of the courses shares the same attributes and methods
        self.name = name
        self.price = price

    def get_name(self):
        return self.name
    def set_price(self, price):
        self.price = price
python = MLCourse("Python", 120)
```

## Problem:

Redundancy, most of the courses shares the same attributes and methods

## Solution

A way to create a blueprint once and other instance should use that as a reference.

## Syntax

Basic Inheritance Syntax

```py
class ParentClass:
    pass

# Inherit from ParentClass
class ChildClass(ParentClass):
    pass
```

## 1. Initialization

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def enroll_student(self):
        return f"Enrolled in {self.name}"

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

class PythonCourse(Course):
    pass
class MLCourse(Course):
    pass

python = PythonCourse("Python", 120)
ml = MLCourse("Python", 120)
ml.set_price(190)
print("ML Price after using set method",ml.get_price())

print("__name__ =",__name__)

```

## 2. Adding New Attributes/Methods to Child Class ()

- When adding new attributes, in `__init__` method inside the child class, the attributes from parent class shall be added first and then the new attribute.
- Using `super().__init__(parent_attributes)`, parent's attribute can be initialized automatically, no need to initialize them again.

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def enroll_student(self):
        return f"Enrolled in {self.name}"

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price


# Adding a unique attributes/method to an instance
class PythonCourse(Course):
    def __init__(self, name, price, duration):
        # Call parent's init method first to avoid initializing them again here (Avoid redundancy)
        super().__init__(name, price)
        self.duration = duration

    def get_duration(self):
        return f"Course duration: {self.duration}"

class MLCourse(Course):
    pass

python = PythonCourse("Python", 120, "4 Weeks")
print(python.get_duration())
ml = MLCourse("Python", 120)
```

### 3. The super() Function

super() allows us to call methods from the parent class.

##### Override

`override`: Child classes can override (replace) parent methods.

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def get_price(self):
        return self.__price

# adding a unique method to an instance
class PythonCourse(Course):
    def __init__(self, name, price, duration):
        # call parent's init method first to avoid initializing them again here (Avoid redundancy)
        super().__init__(name, price)
        self.duration = duration
    # extending the parent's get_price method (Override parent's method)
    def get_price(self):
        parent_price = super().get_price()
        return f"Adding parent's price = {parent_price} to  child price = {super().get_price()} \
parent_price + child price = {parent_price + super().get_price()}"

class MLCourse(Course):
    pass

python = PythonCourse("Python", 120, "4 Weeks")
print(python.get_price())
```

The parent attributes can be accessed via `self.attribute/method` if the attribute is not `private (__attribute_name)`.

```py
class Course:
    def __init__(self, name, price):
        self.name = name
        self.price = price



    def get_price(self):
        return self.__price

# Adding a unique method to an instance
class PythonCourse(Course):
    def __init__(self, name, price, duration):
        # Call parent's init method first to avoid initializing them again here (Avoid redundancy)
        super().__init__(name, price)
        self.duration = duration
    # Extending the parent's get_price method
    def set_price(self, price):
        parent_price = self.price


class MLCourse(Course):
    pass

python = PythonCourse("Python", 120, "4 Weeks")
print(python.get_price())
```

## 6. Multiple Levels of Inheritance

```py
class Course:
    def __init__(self, name):
        self.name = name


class ProgrammingCourse(Course):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def get_info(self):
        return f"{self.language} is from a {self.name} course"

class Framework(ProgrammingCourse):
    def __init__(self, name, language, framework):
        super().__init__(name, language)
        self.framework = framework

    def get_info(self):
        return f"{self.framework} framework is from {self.language} language"

programming = Course("Programming")
python = ProgrammingCourse("Programming","Python")
framework = Framework("Programming","Python","Django")
print(python.get_info())
print(framework.get_info())
```

## 7. Relationship

`isinstance()`: Check if object is instance of a class or checks: `Is this object made from this class (or its parents)?`

`isinstance()` returns True for the object's class AND all its ancestor classes in the inheritance hierarchy!

```sh
Course (base class)
   ↑
   |
ProgrammingCourse (inherits from Course)
   ↑
   |
Framework (inherits from ProgrammingCourse)
```

```py
print(isinstance(framework, Framework))         # True (direct type)
print(isinstance(framework, ProgrammingCourse)) # True (parent)
print(isinstance(framework, Course))            # True (grandparent)
print(isinstance(framework, str))               # False (unrelated)
```

#### `Subclass`

A Class That Inherits from Another Class

It's a class definition, not an object
Created with class `ChildClass(ParentClass)`:

```py
class Course:
    pass

class ProgrammingCourse(Course):  # ProgrammingCourse is a SUBCLASS of Course
    pass
```

## Key Differences Table

| Aspect              | `isinstance()`                         | `issubclass()`                             |
| ------------------- | -------------------------------------- | ------------------------------------------ |
| What it checks      | Objects (instances)                    | Classes                                    |
| First argument      | An object                              | A class                                    |
| Second argument     | A class                                | A class                                    |
| Question it answers | "Is this object made from this class?" | "Does this class inherit from that class?" |

## Multilevel Inheritance

A class can inherit from multiple classes

```py
class Course:
    def __init__(self, name):
        self.name = name

class ProgrammingCourse:
    def __init__(self, language):
        self.language = language

    def get_info(self):
        return f"{self.language}"

class Framework(ProgrammingCourse, Course):
    def __init__(self, name,framework, language):
        ProgrammingCourse.__init__(self,language)
        Course.__init__(self, name)
        self.framework = framework

    def get_info(self):
        return f"{self.framework} framework is from {self.language} language"

python = ProgrammingCourse("Python")
python.language
django = Framework("Programming", "django","python")
print(django.language)
print(django.name)
```

`Key Point`:x Inheritance gives us the methods automatically, but we need to initialize the parent to get its attributes!

## Benefits of Inheritance

| Benefit         | Description                          |
| --------------- | ------------------------------------ |
| Code Reuse      | Don't repeat common code             |
| Organization    | Logical hierarchy of classes         |
| Extensibility   | Easy to add new types                |
| Maintainability | Change parent → all children updated |

---

## Inheritance Terminology

| Term                       | Meaning                                     |
| -------------------------- | ------------------------------------------- |
| Parent / Base / Superclass | Class being inherited from                  |
| Child / Derived / Subclass | Class that inherits                         |
| Override                   | Child replaces parent method                |
| Extend                     | Child adds to parent method using `super()` |
| IS-A relationship          | Child **is a** type of Parent               |
