class Course():
    # Static method - doesn't use 'self' or 'cls'
    @staticmethod
    def get_name(name):
        return name
# Can be called without creating a new object
py = Course.get_name("Python")
print("Result: ", py)
# Can be called with a new object, but not necessary
ml = Course()
print(ml.get_name("Machine learning"))