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

    def get_duration(self):
        return f"Course duration: {self.duration}"
    
class MLCourse(Course):
    pass

python = PythonCourse("Python", 120, "4 Weeks")
print(python.get_duration())
ml = MLCourse("Python", 120)
# print(ml.get_duration()) # Error: get_duration is only defined in python instance

