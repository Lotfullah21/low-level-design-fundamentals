def calc_decorator(func):
    def wrapper(a, b):
        print("Calling Original Function....")
        func(a, b)
        print("Finished Original Function....")
    return wrapper

def add(a, b):
    print(a**b)

res = calc_decorator(add)
res(2,10)