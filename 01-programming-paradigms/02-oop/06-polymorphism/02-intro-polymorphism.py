class PythonCourse:
    # Same method name
    def start(self):  
        print("Starting Python course with coding exercises")

class DesignCourse:
    # Same method name
    def start(self):  
        print("Starting Design course with design projects")

class BusinessCourse:
    # Same method name
    def start(self):  
        print("Starting Business course with case studies")

# Same method name - easy to use!
courses = [PythonCourse(), DesignCourse(), BusinessCourse()]

for course in courses:
    course.start()  # Same method, different behaviors!

# Output:
# Starting Python course with coding exercises
# Starting Design course with design projects
# Starting Business course with case studies