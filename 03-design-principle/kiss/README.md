## 2. KISS (Keep It Simple, Stupid)

`Definition`: Systems work best if they are kept simple rather than made complicated. Avoid cleverness. Code is read much more often than it is written.

#### Where is it used?

- Algorithm design.
- Writing conditions and loops.
- Reviewing code (if you have to ask "what does this line do?", it violates KISS).

#### The Violation (Complex/Over-engineered)

Here, the developer is trying to be "clever" by using a bitwise operator to check for even numbers and a complex one-liner. It works, but it takes 5 seconds to understand.

```py
def check_numbers(numbers):
    # What is happening here?
    # It filters even numbers, but it's hard to read.
    return [n for n in numbers if not n & 1]
```

#### The Solution (KISS)

Write code that a junior developer can understand instantly.

```Python
def check_numbers(numbers):
    # clear, readable, obvious.
    return [n for n in numbers if n % 2 == 0]
```

```py
class DataProcessorFactory:
    @staticmethod
    def create_processor(type):
        if type == "string":
            return StringProcessor()
        elif type == "number":
            return NumberProcessor()

class StringProcessor:
    def process(self, data):
        return data.upper()

# Just to uppercase strings...
```

```py
def process_string(text):
    return text.upper()

def process_number(num):
    return num * 2
```

### Key Benefits:

- Easier to read and understand
- Fewer bugs
- Easier to test and debug
- Faster development
