class PythonCourse:
    def start_python_course(self):
        print("Starting Python course with coding exercises")

class DesignCourse:
    def start_design_course(self):
        print("Starting Design course with design projects")

class BusinessCourse:
    def start_business_course(self):
        print("Starting Business course with case studies")

# Different method names - hard to manage!
python = PythonCourse()
design = DesignCourse()
business = BusinessCourse()

# All methods, same intentions,different name, not nice.
python.start_python_course()    # Different method names
design.start_design_course()    # Different method names
business.start_business_course() # Different method names