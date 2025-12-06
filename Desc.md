# Object-Oriented Programming (OOP) Field Guide

## Quick Definition

> **Object-Oriented Programming** organizes software as a constellation of objects: each object bundles state (data) and behavior (functions declared with `def`) so that we can reason about programs the same way we reason about real-world entities.

```py
def describe_oop():
    pillars = ("abstraction", "encapsulation", "inheritance", "polymorphism")
    return "OOP models problems with collaborating objects driven by " + \
           ", ".join(pillars)

print(describe_oop())
```

## Visual Mental Model

```
+-------------+   instantiates   +---------------+
|    Class    | ---------------> |    Object     |
+-------------+                  +---------------+
        ^ inherits                      ^ collaborates
        |                                |
+-------------+ uses / composes +---------------+
|   Mixin     |---------------->|   Component   |
+-------------+                 +---------------+
```

## Building Blocks at a Glance

| Block       | Definition                                               | Python anchor                   |
| ----------- | -------------------------------------------------------- | ------------------------------- |
| `class`     | Blueprint that groups related state and behavior         | `class Course:`                 |
| `def`       | Declares behavior that objects expose as methods         | `def enroll(self, student):`    |
| `self`      | Reference to the concrete object whose method is running | `self.progress += 1`            |
| `__init__`  | Object constructor; prepares allowed attributes          | `def __init__(self, name):`     |
| `@property` | Controlled attribute access (getter/setter/deleter)      | `@property def duration(self):` |
| `super()`   | Entry point into the parent behavior                     | `super().__init__(name)`        |

## Reference Implementation (Everything in One Place)

```py
from abc import ABC, abstractmethod
from typing import Iterable


class Course(ABC):
    # class attribute shared by all instances
    course_type = "Hybrid"

    def __init__(self, name: str, duration: int, *, level: str = "beginner"):
        self.name = name
        self.level = level
        self._duration = duration
        self._students: list[str] = []

    @property
    def duration(self) -> int:
        return self._duration

    @duration.setter
    def duration(self, months: int) -> None:
        if months < 1:
            raise ValueError("Duration must be at least 1 month.")
        self._duration = months

    def enroll(self, student: str) -> None:
        if student not in self._students:
            self._students.append(student)

    def roster(self) -> tuple[str, ...]:
        return tuple(self._students)

    @abstractmethod
    def platform(self) -> str:
        """Abstraction point; subclasses fill in their delivery medium."""


class OnlineCourse(Course):
    def __init__(self, name: str, duration: int, *, host: str = "Moodle"):
        super().__init__(name, duration, level="intermediate")
        self.host = host

    def platform(self) -> str:
        return f"Streaming on {self.host}"


class Bootcamp(Course):
    def __init__(self, name: str, mentors: Iterable[str]):
        super().__init__(name, duration=3, level="advanced")
        self.mentors = list(mentors)

    def platform(self) -> str:
        return "In-person studio"

    def assign_mentor(self, student: str) -> str:
        mentor = self.mentors[len(student) % len(self.mentors)]
        return f"{student} pairs with {mentor}"


def build_curriculum(*courses: Course) -> list[str]:
    """Combine descriptions to show polymorphism in action."""
    plan = []
    for course in courses:
        plan.append(f"{course.name} ({course.platform()}) -> {course.duration} months")
    return plan


def _demo() -> None:
    python = OnlineCourse("Python OOP", 2, host="Canvas")
    ai = Bootcamp("AI Design Sprint", mentors=("Lina", "Ibrahim", "Mei"))
    for student in ("Ava", "Ravi", "Ava"):
        python.enroll(student)
    ai.enroll("Jon")
    print(build_curriculum(python, ai))
    print(ai.assign_mentor("Jon"))


if __name__ == "__main__":
    _demo()
```

## Core Pillars in One Table

| Pillar            | Definition                                            | Diagnostic question                                       | Code trail                           |
| ----------------- | ----------------------------------------------------- | --------------------------------------------------------- | ------------------------------------ |
| **Abstraction**   | Keep only the essential interface while hiding detail | "What does this object promise?"                          | `@abstractmethod def platform(self)` |
| **Encapsulation** | Bundle state + behavior; guard invariants             | "Who should touch this attribute?"                        | `@duration.setter` validation        |
| **Inheritance**   | Share structure/behavior along a hierarchy            | "Can a generic type implement this so children reuse it?" | `class OnlineCourse(Course)`         |
| **Polymorphism**  | Different classes respond to the same message         | "Can callers treat all variants uniformly?"               | `build_curriculum(course)` loop      |

### Abstraction

> **Definition:** Expose only the signals another object needs, hiding construction details behind method contracts.

```py
class Sensor(ABC):
    @abstractmethod
    def sample(self) -> float:
        ...

def collect(sensor: Sensor) -> float:
     # caller never sees calibration math
    return sensor.sample()
```

### Encapsulation

> **Definition:** Keep related data + methods together and restrict direct manipulation so invariants always hold.

```py
class Battery:
    def __init__(self) -> None:
        self._charge = 100

    @property
    def charge(self) -> int:
        return self._charge

    def drain(self, percent: int) -> None:
        self._charge = max(0, self._charge - percent)
```

### Inheritance

> **Definition:** Specialize behavior by creating a more specific class that reuses code from a parent.

```
           +-------------+
           |   Vehicle   |
           +------+------+
             ^           ^
             |           |
      +------+------+ +--+------+
      | ElectricCar | | Delivery |
      +-------------+ +----------+
```

```py
class Vehicle:
    def start(self):
        print("Engine ready")

class ElectricCar(Vehicle):
    def start(self):
        super().start()
        print("Battery check complete")
```

### Polymorphism

> **Definition:** Send the same message to related objects and let each decide how to respond at runtime.

```
+-----------+    def render()    +-------------+
| Dashboard | -----------------> | Widget ABC  |
+-----------+                    +-------------+
     |   uses def render() implementations in
     |   +------------+  +--------------------+
     +-> | ChartWidget|  | NotificationWidget |
```

```py
class ChartWidget:
    def render(self) -> str:
        return "📈"

class NotificationWidget:
    def render(self) -> str:
        return "🔔"

def paint(widgets: list) -> str:
    return "".join(widget.render() for widget in widgets)
```

## Getter / Setter Checklist

1. Put the raw attribute behind a single underscore to signal "internal" (`self._duration`).
2. Provide a `@property` so callers read naturally (`course.duration`).
3. Add a setter or deleter **only** when external code must mutate the value; otherwise expose behavior methods (`extend_schedule(weeks)`), not naked data.

## Putting It All Together

When designing a feature, ask in order:

1. **Identify nouns** → candidates for classes.
2. **Define verbs** with `def` → behaviors that belong to those nouns.
3. **Group related behaviors** into interfaces/abstract base classes to drive abstraction.
4. **Protect invariants** with encapsulation (properties, private helpers, validation).
5. **Model relationships** with inheritance or composition based on whether you read the requirement as "is-a" (inherit) or "has-a" (compose).
6. **Write polymorphic clients** that depend on behaviors instead of concrete types, so testing and extension stay easy.

Use this README as a quick decision tree: start with the tables, sketch the diagrams to align on relationships, and then lean on the reference implementation whenever you need a working template that demonstrates `def`, code structure, tables, and diagrams in one cohesive OOP narrative.
