#s vs Methods

`Attributes` = Data/properties of an object (variables)
`Methods` = Actions/behaviors of an object (functions)

### 1. Attributes

Attributes Information about course object.

```py
class Course:
    def __init__(self, name, duration, instructor, students_enrolled):
        # attributes
        self.name = name
        self.duration = duration
        self.instructor = instructor
        self.students_enrolled = students_enrolled
        self.is_active = True

course = Course("Python Programming", "8 weeks", "Ahmad", 0)

# Accessing attributes
print(course.name)
print(course.duration)
print(course.instructor)
print(course.students_enrolled)
print(course.is_active)
```

## Methods 2. Methods (Course Actions)

Methods define what we can do with the object.

```py

class Course:
    def __init__(self, name, duration, instructor):
        self.name = name
        self.duration = duration
        self.instructor = instructor
        self.students_enrolled = 0
        self.is_active = True
    # method
    def enroll_student(self):
        self.students_enrolled += 1
        print(f"Student enrolled! Total: {self.students_enrolled}")
    # method
    def start_course(self):
        if self.is_active:
            print(f"Starting {self.name} course with {self.instructor}")
        else:
            print("Course is not active")
    # method
    def complete_course(self):
        self.is_active = False
        print(f"{self.name} course completed!")
    # method
    def get_course_info(self):
        return f"Course: {self.name} | Duration: {self.duration} | Students: {self.students_enrolled}"

course = Course("Python Programming", "8 weeks", "Ahmad")

# calling methods
course.start_course()
course.enroll_student()
course.enroll_student()
print(course.get_course_info())
course.complete_course()
```

## Methods represent actions:

- Enroll a student → enroll_student()
- Start the course → start_course()
- Complete the course → complete_course()
- Get information → get_course_info()

## 4. Types of Attributes

#### 1. - `Instance Attributes` (Different for each course)

- Each course has its own data.

```py
class Course:
    def __init__(self, name, duration, instructor):
        # Instance attribute
        self.name = name
        self.duration = duration
        self.instructor = instructor

course1 = Course("Python Programming", "8 weeks", "Ahmad")
course2 = Course("Web Development", "12 weeks", "Ali")

# each course has its own attributes
print(course1.name) # Python Programming
print(course2.name) # Web Development

print(course1.instructor)  # Ahmad
print(course2.instructor)  # Ali

# changing one doesn't affect the other
course1.name = "Advanced Python"
print(course1.name) # Advanced Python
print(course2.name) # Web Development (unchanged)
```

#### 2. Class Attributes (Shared by all courses)

Some data is the same for all courses.

```py
class Course:
    # class attribute (shared by all courses)
    platform = "Youtube"
    total_courses_created = 0

    def __init__(self, name, duration):
        # instance attribute (unique to each course)
        self.name = name
        self.duration = duration
        # increment for every new course
        Course.total_courses_created += 1

course1 = Course("Python Programming", "8 weeks")
course2 = Course("Web Development", "12 weeks")

# class attribute - same for all courses
print(course1.platform)  # Youtube
print(course2.platform)  # Youtube

# instance attribute - different for each course
print(course1.name)  # Python Programming
print(course2.name)  # Web Development


# changing class attribute affects all
Course.platform = "Coursera"
print(course1.platform)  # Coursera (changed for all)
print(course2.platform)  # Coursera
ml.platform = "Youtube"
```

- `course.platform` → No instance attribute, so uses class attribute → Coursera
- `ml.platform` → Has instance attribute → Youtube (ignores class attribute)

## Summary Table

| Feature       | Attributes                   | Methods                                |
| ------------- | ---------------------------- | -------------------------------------- |
| What they are | Course information (data)    | Course actions (functions)             |
| Syntax        | `course.name`                | `course.enroll_student()`              |
| Purpose       | Store course details         | Perform course operations              |
| Examples      | `name`, `duration`, `price`  | `enroll_student()`, `publish_course()` |
| Access        | No parentheses               | With parentheses                       |
| Think of as   | Properties / characteristics | Abilities / behaviors                  |

---

## Course Object Analogy

- `__Attributes__` = Course information  
  _(name, duration, price, enrolled students)_
- `__Methods__` = Course management  
  _(enroll, publish, rate, apply discount)_

## Instance variable vs class variable

`Class var` = one storage for the whole class
`Instance var` = separate storage for each object

```py
class User:
    # CLASS VARIABLE - shared by all users
    total_users = 0

    def __init__(self, name):
        # INSTANCE VARIABLE - unique to each user
        self.name = name
        User.total_users += 1  # Increment class var

# Usage
user1 = User("John")
user2 = User("Jane")

print(user1.name)  # "John" - instance var (unique)
print(user2.name)  # "Jane" - instance var (unique)

print(User.total_users)  # 2 - class var (shared)
print(user1.total_users)  # 2 - same value (shared)
print(user2.total_users)  # 2 - same value (shared)
```

### Class Variable vs Instance Variable

| Aspect   | Class Variable                    | Instance Variable                   |
| -------- | --------------------------------- | ----------------------------------- |
| Defined  | Inside class, **outside** methods | Inside methods (usually `__init__`) |
| Shared?  | Shared by **ALL** instances       | Unique to **each** instance         |
| Access   | `ClassName.var` or `self.var`     | `self.var`                          |
| Use Case | Counters, constants, singletons   | Object-specific data                |

## What Are Static Methods in Python?

A static method is a function inside a class that:

- Does not receive self (instance)
- Does not receive cls (class)
- Behaves like a regular function, but lives inside a class for organizational reasons

Is defined using the `@staticmethod` decorator
Use static methods when the logic is related to the class, but does not need class or instance data.

```py
class MathTools:
    @staticmethod
    def add(a, b):
        return a + b
```

##### We call it as:

```py
MathTools.add(3, 4)
```

or even:

```py
obj = MathTools()
obj.add(3, 4)
```

## When to Use Static Methods?

- The function logically belongs to the class
- But does not need access to:
- instance attributes (self)
- class attributes (cls)

##### Example use-cases:

- Utility functions
- Validators
- Converters
- Small helpers

### Static Method vs Class Method vs Instance Method

| Method Type     | Receives `self`? | Receives `cls`? | Use Case                            |
| --------------- | ---------------- | --------------- | ----------------------------------- |
| Instance Method | Yes              | No              | Uses instance data                  |
| Class Method    | No               | Yes             | Works with class-level data         |
| Static Method   | No               | No              | Utility/helper logic inside a class |

##### Practical Example

```py
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @staticmethod
    def c_to_f(c):
        return (c * 9/5) + 32

    @staticmethod
    def f_to_c(f):
        return (f - 32) * 5/9
# usage
Temperature.c_to_f(30)
Temperature.f_to_c(86)
```

#### Access to _instance_ attributes → **Instance Method**

```python
class A:
    def test(self):
        print(self.x)  # works, because 'self' refers to the instance
```

#### Access to class attributes → Class Method

```py
class A:
    x = 10
    @classmethod
    def show(cls):
        print(cls.x)
```

#### No need for class/instance data → Static Method

```py
class A:
    @staticmethod
    def add(a, b):
        return a + b
```
