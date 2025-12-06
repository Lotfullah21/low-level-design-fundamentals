## DRY (Don't repeat yourself)

`Principle`: Every piece of knowledge must have a single, unambiguous, authoritative representation within a system.
`Goal`: Reduce repetition of code patterns and logic. When you need to change something, you should only need to change it in one place.

In simple terms: Don't write the same logic twice.

### Where is it used?

- Refactoring functions.
- Defining constants (URLs, Tax Rates, API keys).
- Database configurations.

**The Violation (WET - Write Everything Twice)**

## Example

```py
def area_circle(radius):
    pi = 3.14159
    return pi*radius**2

def area_circle2(radius):
    pi = 3.14
    return pi*radius**2

print(area_circle(2))
print(area_circle2(3))
```

#### The Solution (DRY)

Extract the logic into a single source of truth.

```py
PI = 3.14159
def calculate_circle_area(radius):
    pi = 3.14
    return pi*radius**2

print(calculate_circle_area(1))
print(calculate_circle_area(3))
print(calculate_circle_area(4))
```

## Why it matters

If something changes:

- you change it once
- Fewer bugs
- Cleaner maintenance
