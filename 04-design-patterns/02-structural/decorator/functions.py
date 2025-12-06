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
