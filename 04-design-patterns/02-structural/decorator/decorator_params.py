def repeat(times):
    print(f"1. repeat() called with times={times}")
    
    def decorator(func):
        print(f"2. decorator() called with func={func.__name__}")
        
        def wrapper(*args, **kwargs):
            print(f"3. wrapper() called")
            for i in range(times):
                print(f"   Iteration {i+1}")
                func(*args, **kwargs)
        
        return wrapper
    
    return decorator


@repeat(times=3)
def say_hello():
    print("Hello")

say_hello()