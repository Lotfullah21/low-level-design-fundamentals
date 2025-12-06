class Course:
    def __init__(self, name, price):
        self.name = name
        self.__price = price

    def enroll_student(self):
        return f"Enrolled in {self.name}"
    
    def set_price(self, price):
        self.__price = price
    
    def get_price(self):
        return self.__price

# Adding a unique method to an instance
class PythonCourse(Course):
    def __init__(self, name, price, duration):
        # Call parent's init method first to avoid initializing them again here (Avoid redundancy)
        super().__init__(name, price)
        self.duration = duration
    # Extending the parent's get_price method
    def get_price(self):
        parent_price = super().get_price()
        return f"Adding parent's price = {parent_price} to  child price = {super().get_price()} \
parent_price + child price = {parent_price + super().get_price()}"
    
class MLCourse(Course):
    pass

python = PythonCourse("Python", 120, "4 Weeks")
print(python.get_price())

print(python.__dict__) 
# Accessing private attributes
print(python._Course__price)