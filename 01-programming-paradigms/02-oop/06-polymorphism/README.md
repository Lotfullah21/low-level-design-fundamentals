## What is Polymorphism?

Polymorphism means "many forms" (poly = many, morph = form).

In programming, it means:

- The same method name can have different behaviors in different classes
- Different objects can respond to the same method call in their own way

## Types of Polymorphism

#### 1.Method Overriding (Runtime Polymorphism):

Child classes override parent's method with their own implementation.

```py
class Course:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Starting {self.name} course")

class PythonCourse(Course):
    # override parent's method
    def start(self):
        print(f"Starting {self.name} with Python interpreter setup")

class DesignCourse(Course):
    def start(self):
        print(f"Starting {self.name} with design tools installation")

# same method name, different behaviors
python = PythonCourse("Python Programming")
design = DesignCourse("UI/UX Design")

python.start()  # Starting Python Programming with Python interpreter setup
design.start()  # Starting UI/UX Design with design tools installation
```

#### 2. Method Overloading (Compile-time Polymorphism)

Python doesn't support traditional method overloading like Java/C++, but we can simulate it with default arguments or \*args.

Method Overloading is when we have multiple methods with the same name but different parameters (different number or types of arguments).

###### Method Overloading in Other Languages (Java, C++)

In languages like Java or C++, you can have multiple methods with the same name:

```java
// Java example
class Calculator {
    // Method 1: Add two integers
    int add(int a, int b) {
        return a + b;
    }

    // Method 2: Add three integers
    int add(int a, int b, int c) {
        return a + b + c;
    }

    // Method 3: Add two doubles
    double add(double a, double b) {
        return a + b;
    }
}

Calculator calc = new Calculator();
calc.add(1, 2);        // Calls method 1
calc.add(1, 2, 3);     // Calls method 2
calc.add(1.5, 2.5);    // Calls method 3
```

#### Python Does NOT Support Traditional Method Overloading!

In Python, if you define multiple methods with the same name, the last one overwrites the previous ones:

```py

class Calculator:
    def add(self, a, b):
        return a + b

    # ← This OVERWRITES the previous add()
    def add(self, a, b, c):
        return a + b + c

calc = Calculator()
calc.add(1, 2)     # TypeError: add() missing 1 required positional argument: 'c'
calc.add(1, 2, 3)  # Works: 6
```

#### How to Achieve Overloading in Python

Python offers several alternatives:

###### 1. Default Arguments (Most Common)

python

```py
class Calculator:
def add(self, a, b, c=0): # c has a default value
return a + b + c

calc = Calculator()
print(calc.add(1, 2))
print(calc.add(1, 2, 3))
```

###### 2. Variable-Length Arguments `(*args)`

```py
class Calculator:
    # accept any number of arguments
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(1, 2))           #  3
print(calc.add(1, 2, 3))        #  6
print(calc.add(1, 2, 3, 4, 5))  #  15
```
