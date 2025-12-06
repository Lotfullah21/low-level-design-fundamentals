## `__main__` function

When python runs a file, it creates a variable called `__name__`

- If the file is run directly, `__name__` equals `__main__`
- If the file is imported as a module, `__name__` equals the module's name

1. If the file main is gets executed, like `python file.py`, the `__name__` value is `__main__`
2. If the file is imported into a file named `file2` like `import get_info`, the `__name__` when running the `file2` will be like this.
   1. file2 is executed directly, hence `__name__ == __main__`
   2. file1 is imported, hence, `__name__ == file1.py`

```py
from file1 import get_info

print(f"__name__ in file2: {__name__}")
print("From File 1")
get_info("hello")
```

```py
def get_info(name:str) ->str | None:
    print(name)

print(f"__name__ in file1: {__name__}")
print("From file 1")
get_info("ali")
```

| File       | How It's Used          | `__name__` Value |
| ---------- | ---------------------- | ---------------- |
| `file1.py` | Imported by `file2.py` | `"file1"`        |
| `file2.py` | Run directly           | `"__main__"`     |

## Problem

Whatever is called in file1 runs automatically when we import file1, even though we only wanted the `get_info()` to run.

## Solution

Use `__main__` as the checking point, the `__name__` variable tells you whether the file is the "main program" or just a module being imported!

```py
class Course:
    def __init__(self, name, duration):
        self.name=name
        self.duration = duration

def main():
    python = Course("Python", "3 months")
    ml = Course("Machine learning", "4 months")
    print(python.name)
    print(ml.name)


# this make sure to execute __main__ only if the file is executed directly
if __name__ == "__main__":
    main()
```

```py
from main_file import main

print(f"__name__ in module_file: {__name__}")
```

## File vs Module

In Python, a module IS a file - but not every file becomes a module in the same way.

### 1. File

- A .py file on the computer
- Just a text file with Python code

### 2. Module

- A file that is being imported and used by another file
- When we import a file, it becomes a module

1. The file that imports like file2 = Main script / Main program
2. The file being imported like file1 or main_file = Module

| File       | Role               | `__name__` Value | What It's Called           |
| ---------- | ------------------ | ---------------- | -------------------------- |
| `file1.py` | Being imported     | `"file1"`        | Module                     |
| `file2.py` | Being run directly | `"__main__"`     | Main script / Main program |
