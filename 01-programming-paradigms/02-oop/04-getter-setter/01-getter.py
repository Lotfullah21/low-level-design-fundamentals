class Course:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price
    
    # Getter for name
    def get_name(self):
        return self.__name
    
    # Setter for name (with validation)
    def set_name(self, new_name):
        if new_name.strip():  # Not empty
            self.__name = new_name
        else:
            print("Name cannot be empty")
    
    # Getter for price
    def get_price(self):
        return self.__price
    
    # Setter for price (with validation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Price must be positive")

course = Course("Python", 99)

# Use getters
print(course.get_name())   # Python
print(course.get_price())  # 99

# Use setters
course.set_name("Advanced Python")
course.set_price(149)

print(course.get_name())   # Advanced Python
print(course.get_price())  # 149

# Validation works
course.set_name("")        # Name cannot be empty
course.set_price(-50)      # Price must be positive