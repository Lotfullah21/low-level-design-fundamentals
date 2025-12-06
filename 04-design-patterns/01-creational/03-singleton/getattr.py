class Person:
    def greet(self):
        return "Hello"

p = Person()
# It returns the method object with an address, not the result of calling it.
print(getattr(p, "greet")) 