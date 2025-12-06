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

class PythonCourse(Course):
    pass
class MLCourse(Course):
    pass

python = PythonCourse("Python", 120)
ml = MLCourse("Python", 120)
ml.set_price(190)
print("ML Price after using set method",ml.get_price())

print("__name__ =",__name__)

