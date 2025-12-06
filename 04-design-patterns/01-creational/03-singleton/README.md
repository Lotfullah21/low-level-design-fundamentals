## Singleton

- `What`: One shared instance/global access point, Only ONE instance exists globally
- `Where in Django`: Database connection, config, logger
- `django.conf.settings` (module-as-singleton), DB backend registry.
- `Pros`: simple shared config; avoids repeated setup,Share one instance, save resources.
- `Cons`: implicit global state hurts tests; avoid for connections—use pools/factories.

We can create only one single object.

Just like a global variable, the Singleton pattern lets us access some object from anywhere in the program. However, it also protects that instance from being overwritten by other code.

### When to use singleton

- Creating objects are expensive
- For shared resources
- When classes have only few methods

### Where used:

- Database connections
- App configuration

### How to Create Singleton in Python

What is `__new__`?

- `__new__` is the constructor that creates the object before `__init__` runs.
- `__new__` creates the object (allocates memory).
- `__init__` initializes the object (sets values).
- `cls` means the class itself, just like `self` means the object.

### Why do we call super().`__new__(cls)`?

Because only the parent class (object) knows how to actually create a new instance in memory.

object.`__new__()` is the built-in low-level function that:

- allocates memory
- creates an empty instance
- returns it

### What is object?

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

```py
class DatabaseConnection:
    _instance = None
```

Python turns it into:

```py
class DatabaseConnection(object):
    _instance = None
```

### Why does object matter?

Singleton uses:

```py
# Hey parent class (object), please create a new instance of DatabaseConnection
super().__new__(cls) # super() returns the parent class
```

cls means the class we are creating,

This effectively calls:

```py
object.__new__(cls)
```

```py
print(DatabaseConnection.__bases__)
```

```py
# settings is imported once; values are globally accessible
from django.conf import settings
if settings.DEBUG:
    pass
```

#### getattr()

`getattr()` returns the value of an attribute from an object.

```py
getattr(object, "attribute_name", default_value)
```

- object → the object to look at
- "attribute_name" → a string
- default_value (optional) → returned if the attribute does NOT exist

```py
class Person:
    name = "Ahmad"

print(getattr(Person, "name"))
```

```py
class Person:
    def greet(self):
        return "Hello"
p = Person()
print(getattr(p, "greet")) # <bound method Person.greet of <Person object>>
```

Use module-level instances instead of Singleton pattern. It's simpler and more Pythonic.

```py
# config.py
class Config:
    def __init__(self):
        self.debug = True
# module-level = natural singleton
config = Config()
# just import it
from config import config
```

## How to create a singleton object:

- ## 1. Using `_private` attribute

```py
class DatabaseConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            # initialize only once
            cls._instance.connection = "Connected to PostgreSQL"
        return cls._instance
# usage
db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)
print(id(db1) == id(db2))
```

- ## 2. Using module level class (pythonic way)

```py
# config.py
class _AppConfig:
    def __init__(self):
        self.database_url = "postgresql://localhost/mydb"
        self.redis_url = "redis://localhost:6379"
        self.debug = True

    def get(self, key):
        return getattr(self, key, None)

# create single instance at module level
app_config = _AppConfig()
```

In another file

```py
# settings.py

# usage in other files
from config import app_config
print(app_config.database_url) # always same instance.

```

How it works?

```py
cls._instance = super().__new__(cls)
#      ↑                    ↑
#      |                    └─ Create new instance
#      └─ Store it in class variable _instance
```

- `super().__new__(cls)` → Creates a new instance
- `cls._instance = ...` → Stores that instance in the class variable
- `cls._instance._load_config()` → Uses the stored instance to call method

##### Visual Flow

```sh
# first call
config1 = ConfigManager()
    ↓
cls._instance is None? YES
    ↓
Create new instance: super().__new__(cls)
    ↓
Store it: cls._instance = new_instance
    ↓
Configure it: cls._instance._load_config()
    ↓
Return it: return cls._instance

# second call
config2 = ConfigManager()
    ↓
cls._instance is None? NO (already exists!)
    ↓
Return existing: return cls._instance  ← Same instance as config1!

```

## Important

# Python Module Naming Rules

**Rule:** A module name must start with a **letter or underscore**, and contain only **letters, digits, and underscores**.

| Status     | Module Name                                                                                                |
| ---------- | ---------------------------------------------------------------------------------------------------------- |
| ✅ Valid   | `config.py`                                                                                                |
| ❌ Invalid | `05-config.py`                                                                                             |
| ❌ Invalid | `my-config.py`                                                                                             |
| ❌ Invalid | `config manager.py`                                                                                        |
| ❌ Invalid | `2config.py`                                                                                               |
| ✅ Valid   | `_config.py` → (Actually valid name, but depends on your intention: leading underscore suggests "private") |
| ✅ Valid   | `app_config.py` → (Actually valid — no rule broken)                                                        |
| ✅ Valid   | `config_manager.py` → (Actually valid — no rule broken)                                                    |

---

## Correction of Valid/Invalid Classification

Based strictly on Python’s module naming rules:

### These are actually **valid**:

```python
config.py
app_config.py
config_manager.py
_config.py

## Resources

[Singleton-patterns](https://refactoring.guru/design-patterns/singleton)
```
