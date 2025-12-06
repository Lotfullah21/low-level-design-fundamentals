def calc_decorator(func):
    def wrapper():
        print("Calling Original Function....")
        func()
        print("Finished Original Function....")
    return wrapper

def add():
    print(12+12)

res = calc_decorator(add)
res()