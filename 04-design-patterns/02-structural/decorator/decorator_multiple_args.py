def calc_decorator(func):
    def wrapper(*args,**kwargs):
        print("Calling Original Function....")
        func(*args,**kwargs)
        print("Finished Original Function....")
    return wrapper

def add(c, a, b):
    print(a**b)

res = calc_decorator(add)
res(12, a=2,b=10)