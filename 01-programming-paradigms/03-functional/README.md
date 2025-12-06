## 3. Functional Programming

Treat computation as the evaluation of mathematical functions.

### Characteristics:

- Pure functions (no side effects)
- Immutable data
- Functions as first-class citizens

## 1. Pure Functions (No Side Effects)

A pure function:

- Always returns the same output for the same input
- Doesn't modify anything outside itself (no side effects)
- Doesn't depend on external state

```py
# PURE FUNCTION
def add(a, b):
    return a + b

result1 = add(2, 3)  # Always 5
result2 = add(2, 3)  # Always 5
# No side effects, predictable
```

An Impure Function

```py
# IMPURE FUNCTION (has side effects)
total = 0

def add_to_total(value):
    global total
    # Modifies external state (side effect!)
    total += value
    return total

result1 = add_to_total(5)  # 5
result2 = add_to_total(5)  # 10 (different result with same input!)
# Has side effects, unpredictable
```

### Side effects include:

- Modifying global variables
- Changing input parameters
- Printing to console
- Writing to files
- Making network requests

#### 2. Immutable Data

Data cannot be changed after creation. Instead, create new data.

```py
# MUTABLE (Procedural/OOP style)
numbers = [1, 2, 3]
numbers.append(4)  # Modifies original list
print(numbers)     # [1, 2, 3, 4]
```

# IMMUTABLE (Functional style)

```py
numbers = [1, 2, 3]
# Creates NEW list
new_numbers = numbers + [4]
print(numbers) # [1, 2, 3] (original unchanged)
print(new_numbers) # [1, 2, 3, 4]
```

### 3. Functions as First-Class Citizens

Functions can be:

- Assigned to variables
- Passed as arguments to other functions
- Returned from other functions

```py
def greet(name):
    return f"Hello, {name}"

# assign function to a variable
say_hello = greet
print(say_hello("ahmad"))  # Hello, ahmad
```

#### B. Pass functions as arguments (Higher-Order Functions)

```py
def apply_operation(x, y, operation):
    # call the function passed in
    return operation(x, y)

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

result1 = apply_operation(5, 3, add)       # 8
result2 = apply_operation(5, 3, multiply)  # 15
```

#### C. Return functions from other functions

```py
def create_multiplier(factor):
    def multiplier(x):
        return x * factor
    # Return a function
    return multiplier

times_two = create_multiplier(2)
times_five = create_multiplier(5)

print(times_two(10))   # 20
print(times_five(10))  # 50
```

# Functional vs Procedural Programming

## Key Differences

| Aspect       | Procedural Programming        | Functional Programming               |
| ------------ | ----------------------------- | ------------------------------------ |
| State        | Modifies state/variables      | Avoids changing state                |
| Data         | Mutable (can change)          | Immutable (cannot change)            |
| Functions    | Can have side effects         | Pure functions only                  |
| Control Flow | Loops (`for`, `while`)        | Recursion, `map`, `filter`, `reduce` |
| Focus        | "How" to do something (steps) | "What" to compute (transformations)  |

### Example: Calculate sum of squares

Procedural Style

```py
# uses loops, modifies state
numbers = [1, 2, 3, 4, 5]
# mutable state
total = 0

for num in numbers:
    # modifies 'total'
    total += num ** 2

print(total)  # 55
```

### Functional Style

```py
# uses pure functions, no state modification
numbers = [1, 2, 3, 4, 5]

def square(x):
    return x ** 2

# chain transformations
squared = map(square, numbers)
total = sum(squared)

print(total)  # 55
```

## Another example

```py
# IMPURE - has side effects
def greet(name):
     # side effect: outputs to console
    print(f"Hello {name}")
    with open('log.txt', 'a') as f:
        # side effect: writes to file
        f.write(f"Greeted {name}\n")
    return f"Hello {name}"
```

These are side effects because the function does more than just compute and return a value - it changes the outside world (console output, file on disk).

### Simple rule:

If a function interacts with anything outside itself (screen, files, network, global variables), it's a side effect!

#### Benefits of Functional Programming

- Easier to test - Pure functions always give same output for same input
- Easier to debug - No hidden state changes
- Parallel execution - No shared state means safe concurrency
- More predictable - Functions don't have surprising side effects
