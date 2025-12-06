## Decorator Pattern

It is a Structural Design Pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

## 1. Functions are objects

In python,Functions are first class objects, can be passed around like variables.

```py
def greet():
    return "Hello"
# Assign to variable
my_func = greet
print(my_func()) # "Hello"
```

## 2. Functions Can Return Functions

```py
def outer_function():
    def inner_function():
        return "I'm inside!"
    return inner_function  # Return the function itself

# Get the inner function
my_func = outer_function()
print(my_func)      # <function inner_function at 0x...>
print(my_func())    # "I'm inside!"
```

## 3. Functions Can Take Functions as Arguments

```py
def calc(func,a,b):
    print("Before calling the inner function")
    result = func(a, b)
    print("Result: ", result)
    print("After calling inner function")

def add(a, b):
    return a + b
def mul(a,b):
    return a*b

calc(mul, 12, 100)
```

## Decorator

A decorator is just a function that:

- Takes a function as input
- Returns a new function that wraps the original function

```py
# calc is the decorator
def calc(func):
    def wrapper():
        print("Calling Original Function....")
        func()
        print("Finished Original Function....")
    return wrapper

def add():
    print(12+12)

res = calc(add)
res()
```

## The @ Syntax is Just Shorthand

```py
# This:
@my_decorator
def say_hello():
    return "Hello!"

# Is EXACTLY the same as:
def say_hello():
    return "Hello!"
say_hello = my_decorator(say_hello)
```

## Accepting Arguments

Using `*args` and `**kwargs`, multiple arguments can be passed to the wrapper.

```py
def calc_decorator(func):
    def wrapper(*args,**kwargs):
        print("Calling Original Function....")
        func(*args,**kwargs)
        print("Finished Original Function....")
    return wrapper

def add(c, a, b):
    print(a**b)

res = calc_decorator(add)
res(12, a=2,b=10)
```

Decorators wrap functions, adding behavior before/after the original function runs.

```py

def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    print("Hello")

say_hello()
```

```py
@repeat(times=3)
def say_hello():
    print("Hello")

# Execution order:
# 1. repeat(3) is called → returns decorator
# 2. decorator(say_hello) is called → returns wrapper
# 3. say_hello is now wrapper
# 4. When we call say_hello():
#    → wrapper runs
#    → loops 3 times
#    → calls original say_hello each time
```

## How variable reassignment happens?

The line of code:

```py
@my_decorator
def say_hello():
    print("Hello")
```

This explicit reassignment is where the process begins.

```py
def say_hello():
    print("Hello")
# This explicit reassignment is where the process begins.
say_hello = my_decorator(say_hello)
```

## Preserving Metadata (functools.wraps)

When we use a decorator, the wrapper function replaces the original function. This means the original function's metadata (name, docstring, parameter list) is lost, and the debugger sees only the generic wrapper function.

```py
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

# Problem: Metadata is lost!
# print(add.__name__)  # Output: 'wrapper'
# print(add.__doc__)   # Output: None
```

## The Problem

If we call the decorated function and check its name, we get the generic name of the wrapper function:

## The Solution: @functools.wraps

The standard library provides @functools.wraps to fix this. It's a decorator itself, which copies the relevant metadata from the original function to the wrapper function

```py
import functools

def my_decorator(func):
    # Apply @wraps to the wrapper function
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        """This docstring will be copied."""
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

# Solution: Metadata is preserved!
# print(add.__name__)  # Output: 'add'
# print(add.__doc__)   # Output: 'Adds two numbers.'
```

## 2. Class Decorators

A function decorator wraps a function, but a Class Decorator wraps an entire class.

When Python executes a class definition, it treats the class object like any other object. Therefore, the `@` syntax can be used to pass the entire class object to a decorator function, which then returns a modified class object.

```py
def add_timestamp(cls):
    """
    This decorator takes a class object (cls) as input.
    It returns a modified class object.
    """
    # 1. Define a new method to be added to the class
    def timestamp(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")

    # 2. Add the new method to the class dynamically
    cls.timestamp = timestamp

    # 3. Return the modified class
    return cls

@add_timestamp
class Event:
    def __init__(self, name):
        self.name = name

# Usage:
event = Event("Meeting")
print(event.timestamp()) # Output: (Current time string)
```

# 🎁 Real-World Use Cases of the Python Decorator Pattern

The Decorator Pattern is used to cleanly apply **cross-cutting concerns**—logic that applies to many different functions or classes—without modifying their core code.

## 1. Web Framework Functionality (Security & Routing)

Decorators are essential in Django and other frameworks to manage the request/response flow and enforce access rules on views.

| Scenario               | Goal                                                        | Django Example                            | Mechanism                                                                                           |
| :--------------------- | :---------------------------------------------------------- | :---------------------------------------- | :-------------------------------------------------------------------------------------------------- |
| **Authentication**     | Restrict access to logged-in users.                         | `@login_required`                         | The wrapper function checks the session and redirects if the user is anonymous.                     |
| **Authorization**      | Check for specific user permissions.                        | `@permission_required('app.can_edit')`    | The wrapper verifies the user's role before allowing the view logic to execute.                     |
| **Method Restriction** | Limit the HTTP methods accepted by an endpoint.             | `@require_POST`                           | The wrapper checks the request method; returns 405 (Method Not Allowed) if invalid.                 |
| **Route Registration** | Assign a function to a URL path during application startup. | `@app.route('/products')` (Flask/FastAPI) | The class decorator registers the function and its URL path with the application's router registry. |

## 2. Data Integrity & Transactions

Decorators provide a clean way to manage critical database boundaries, typically used in the Service Layer.

| Scenario                 | Goal                                                                                                | Django Example        | Mechanism                                                                                    |
| :----------------------- | :-------------------------------------------------------------------------------------------------- | :-------------------- | :------------------------------------------------------------------------------------------- |
| **Transaction Boundary** | Ensure a series of database operations either all succeed (COMMIT) or all fail (ROLLBACK) together. | `@transaction.atomic` | The wrapper function runs the decorated code inside a guaranteed database transaction block. |

## 3. Performance & Caching

Decorators are the simplest tool for adding non-invasive performance enhancements to functions.

| Scenario                | Goal                                                                                   | Python Example                      | Mechanism                                                                                                  |
| :---------------------- | :------------------------------------------------------------------------------------- | :---------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Function Caching**    | Store the result of an expensive function call in memory based on its input arguments. | `@functools.lru_cache(maxsize=128)` | The wrapper checks its cache for the arguments first; executes the original function only on a cache miss. |
| **Property Conversion** | Transform a class method into a read-only attribute for cleaner access.                | `@property`                         | The wrapper allows the method to be called without parentheses (`instance.attribute`).                     |

## 4. Auditing, Logging, and Debugging

Used to apply boilerplate auditing code consistently across numerous functions.

| Scenario               | Goal                                                                    | Custom Decorator Example   | Mechanism                                                                                                 |
| :--------------------- | :---------------------------------------------------------------------- | :------------------------- | :-------------------------------------------------------------------------------------------------------- |
| **Logging/Profiling**  | Automatically log execution time, function inputs, and outputs.         | `@log_execution_time`      | The wrapper captures the start time, executes the function, calculates the duration, and logs the result. |
| **Class Registration** | Automatically configure or modify a class structure when it is defined. | `@admin.register` (Django) | The decorator takes the class object, performs necessary setup, and returns the modified class.           |
