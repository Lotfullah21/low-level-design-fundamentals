## Programming paradigms

A programming paradigm is an approach/style for writing code

### Main Programming Paradigms

- Procedural Programming - Step-by-step instructions (like a recipe)
- Object-Oriented Programming (OOP) - Organizing code around objects
- Functional Programming - Using pure functions and avoiding state changes
- Declarative Programming - Describing what you want, not how to do it

#### 1. Procedural Programming

Write code as a sequence of steps/procedures.

```py
def start(name):
    print(f"Starting, {name}")

def watch_videos(name):
    print(f"Watching videos of {name} course")

def finish_course(name, duration):
    print(f"Finished {name} course after {duration}")

name = input("Enter the course: ")

duration = input("Enter the duration: ") + " weeks"

start(name)
watch_videos(name)
finish_course(name, duration)
```

### Characteristics:

- Linear flow of execution
- Functions operate on data
- Data and functions are separate

## Why Do We Need Different Paradigms?

Different problems are easier to solve with different approaches:

- Procedural: Simple scripts, automation tasks
- OOP: Complex applications with many entities (games, GUIs, enterprise apps)
- Functional: Data transformations, concurrent programming

The Four Pillars of OOP:

Encapsulation (hiding data)
Inheritance (creating child classes)
Polymorphism (same method, different behaviors)
Abstraction (hiding complexity)

Special methods (**str**, **repr**, **len**, etc.)
Property decorators (@property, getters/setters)
