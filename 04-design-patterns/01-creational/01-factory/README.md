## Factory Method Pattern

The Factory Method Pattern is when you define a method for creating objects, but let subclasses decide which class to instantiate.
Creates objects without exposing creation logic. Returns different types based on input.
Instead of calling new Product() directly in your code, you call a method that creates the product for you and the method is called `factory method`.

Rule: If you have 3+ similar classes to create, use Factory.

## Terminalogies

**Factory**: Any code that creates objects, Function or class that returns objects
**Factory Method**: It is the method that creates objects, in other words, it is an abstract method that subclasses override to create products
**Creator**: The class tha contains factory method
**Product**: The object we are trying to create. In a car factory, the product will be a car.
**Abstract Product**: Means not the actual product, just the idea. a vehicle is an abstract product, but a car is an actual product
**Concrete Product**: Concrete means specific or actual implementation and the concrete product is the actual object with the code

#### @staticmethod:

A function that lives inside a class and don't need to access to the class or to the object.
**When to use**: When the function doesn't need to access any instance data or class data.

#### @classmethod:

The class itself is passed to a method with the name `cls` as the first argument, not an instance.
**When to use**: When you need to access or modify class-level data, or create instances in different ways.

#### @abstractmethod

An abstract method is a method that must be implemented by subclasses. It's like a promise: "If you inherit from me, you MUST implement this method."

We need to import it from the abc module (Abstract Base Classes).

**When to use**: When you want to ensure all subclasses implement certain methods.

### override

Override means to replace a method from the parent class with a new implementation in the child class.

Override = Replace parent's method with your own version

## Key Characteristics of Factory Method

### 1. Defers object creation to subclasses

- The parent class doesn't decide what to create - children do.

### 2. Single Responsibility

- `Creator class: business logic`
- `Factory method: object creation`

### 3. Open/Closed Principle

- Open for extension: add new products by creating new subclasses
- Closed for modification: don't change existing code

## When to Use Factory Method

#### Use when:

- You don't know ahead of time which exact class you need to create
- You want subclasses to specify which objects to create
- You want to delegate object creation responsibility
- A class wants its subclasses to specify the objects it creates

#### Don't use when:

- You only have one product type
- Object creation is simple and won't change
- Adding complexity doesn't add value

## Factory Method Pattern:

**Intent**: Define an interface for creating objects, but let subclasses decide which class to instantiate
**Main idea**: Use inheritance to decide what to create
**Factory method**: Abstract method that subclasses override to create products
**Benefit**: Loose coupling, easy to extend with new product types

## Factory Method vs Simple Factory

```py
# SIMPLE FACTORY - just a function/method that creates objects
class SimpleFactory:
    @staticmethod
    def create_transport(transport_type):
        if transport_type == 'truck':
            return Truck()
        elif transport_type == 'ship':
            return Ship()
        # All creation logic in ONE place

# FACTORY METHOD - uses inheritance and polymorphism
class Logistics(ABC):
    @abstractmethod
    def create_transport(self):
        pass
    # Each SUBCLASS has its own creation logic
```

### Difference:

- Simple Factory: One class/function creates all products
- Factory Method: Each subclass creates one type of product

That's It!

## 5 Steps:

- Base class (abstract)
- Concrete classes (implementations)
- Factory class (with dictionary)
- Map types → classes
- Use it

### Pythonic Template

```py
from abc import ABC, abstractmethod

# Step 1: Base class
class YourBase(ABC):
    @abstractmethod
    def method1(self):
        pass

# Step 2: Concrete classes
class Type1(YourBase):
    def __init__(self, **kwargs):
        # Initialize attributes
        pass

    def method1(self):
        # Implementation
        pass

class Type2(YourBase):
    def __init__(self, **kwargs):
        pass

    def method1(self):
        pass

# Step 3: Factory
class YourFactory:
    @staticmethod
    def create(type_name, **kwargs):
        types = {
            'type1': Type1,
            'type2': Type2
        }

        object = types.get(type_name)
        if not object:
            raise ValueError(f"Unknown type: {type_name}")

        return object(**kwargs)

# Step 4: Use it
obj = YourFactory.create('type1', param1='value1')
```

```py
from abc import ABC, abstractmethod

# Step 1: Abstract base class
class Content(ABC):
    @abstractmethod
    def render(self) -> str| None:
        pass
    @abstractmethod
    def validate(self) -> bool| None:
        pass

# Step 2: Create concrete class
class VideoContent(Content):
    def __init__(self, title, url):
        self.title:str = title
        self.url:str = url

    def render(self):
        return f"<video>{self.url}</video>"

    def validate(self):
        return self.url.endswith((".mp4", ".mov"))


class QuizContent(Content):
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions

    def render(self):
        return f"<h1>{self.title}</h1>"

    def validate(self) -> bool | None:
        return super().validate()

# Step 3: Create factory class
class ContentFactory:
    @staticmethod
    def create(content_type, **kwargs):
        types = {
            "quiz":QuizContent,
            "video":VideoContent,
        }
        object = types.get(content_type)
        if not object:
            raise ValueError(f"Unknown content type: {content_type}")
        return object(**kwargs)

video = ContentFactory.create("video",title = "Intro to functions",url="https://youtu.be/8TRijfkvUfQ?si=BX_RwN_LaLpW2DM4")
quiz = ContentFactory.create("quiz",title="Python basics",questions="https://youtu.be/8TRijfkvUfQ?si=BX_RwN_LaLpW2DM4")

print(video.validate())
print(video.render())
```

In Django, we don't usually create separate "Factory" classes. Instead, we put that creation logic inside the Model Manager (objects).

## The Django Translation

We will use Proxy Models to keep the specific behavior for Python vs. Java and a Custom Manager to handle the factory creation.

```py
from django.db import models

# 1. The Manager (Acts as the Factory)
# This replaces 'CourseFactory', 'PythonCourse' (creator), and 'JavaCourse' (creator)
class CourseManager(models.Manager):
    def create_course(self, course_type, name):
        """
        This is the factory method. It decides which class
        to instantiate based on the type string.
        """
        if course_type == 'python':
            return Python.objects.create(name=name)
        elif course_type == 'java':
            return Java.objects.create(name=name)
        else:
            raise ValueError("Unknown Course Type")

# 2. The Base Model (Acts as the Abstract Product)
# This replaces the 'Course' abstract base class
class Course(models.Model):
    # Data fields (State)
    name = models.CharField(max_length=100)
    course_type = models.CharField(
        max_length=10,
        choices=[('python', 'Python'), ('java', 'Java')]
    )

    # Attach the factory manager
    objects = CourseManager()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Base save logic
        super().save(*args, **kwargs)

# 3. Proxy Models (Act as Concrete Products)
# These allow different behaviors (methods) for the same database table
class Python(Course):
    class Meta:
        proxy = True # This tells Django not to make a new DB table

    def save(self, *args, **kwargs):
        self.course_type = 'python'
        print("🐍 Saving Python specific logic...")
        super().save(*args, **kwargs)

class Java(Course):
    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.course_type = 'java'
        print("☕ Saving Java specific logic...")
        super().save(*args, **kwargs)

```

## How to use it

```py
# Create a Python course
# The Manager handles the logic of which class to init
c1 = Course.objects.create_course('python', name="Django 101")
# Output: 🐍 Saving Python specific logic...

# Create a Java course
c2 = Course.objects.create_course('java', name="Spring Boot 101")
# Output: ☕ Saving Java specific logic...
```
