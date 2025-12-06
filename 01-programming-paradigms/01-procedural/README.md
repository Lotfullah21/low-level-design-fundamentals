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

### Data and Functions are Separate (Procedural)

In procedural programming, data exists independently, and functions operate on that data from the outside.

```py

# DATA - stored separately
account_balance = 1000
account_holder = "Alice"

# FUNCTIONS - operate on the data from outside
def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds")
        return balance

def get_balance(balance):
    return balance

# Using them separately
account_balance = deposit(account_balance, 500)
print(f"Balance: {account_balance}")  # 1500

account_balance = withdraw(account_balance, 200)
print(f"Balance: {account_balance}")  # 1300
```

### Problem:

- The data (account_balance) and functions (deposit, withdraw) are disconnected
- Any part of the code can accidentally modify account_balance
- We have to manually pass data to functions every time

Procedural = Having ingredients (data) in one place and recipes (functions) in another. You have to fetch ingredients and bring them to the recipe book every time.

## Languages

`C + +` and `C`
