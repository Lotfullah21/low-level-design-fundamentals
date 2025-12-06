class Course:
    def __init__(self, name):
        self.name = name
        print("Course created!")

dog = Course("ML")  # __init__ runs automatically
# Output: "Course created!"