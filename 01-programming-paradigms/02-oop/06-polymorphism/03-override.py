class Course:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"Starting {self.name} course")

class PythonCourse(Course):
    # Override parent's method
    def start(self):
        print(f"Starting {self.name} with Python interpreter setup")

class DesignCourse(Course):
    def start(self):
        print(f"Starting {self.name} with design tools installation")

# Same method name, different behaviors
python = PythonCourse("Python Programming")
design = DesignCourse("UI/UX Design")

python.start()  # Starting Python Programming with Python interpreter setup
design.start()  # Starting UI/UX Design with design tools installation