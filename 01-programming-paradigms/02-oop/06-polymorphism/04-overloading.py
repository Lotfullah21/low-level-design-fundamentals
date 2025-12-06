class Course:
    def __init__(self, name):
        self.name = name
    
    # simulate overloading with default arguments
    def enroll(self, student_name, is_premium=False):
        if is_premium:
            print(f"Premium enrollment: {student_name} in {self.name}")
        else:
            print(f"Regular enrollment: {student_name} in {self.name}")

course = Course("Python Programming")

# same method, different number of arguments
course.enroll("Ahmad")             
course.enroll("Ali", True)        