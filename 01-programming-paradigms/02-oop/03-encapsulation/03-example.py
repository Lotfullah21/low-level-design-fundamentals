class Course:
    def __init__(self, name, price, max_students):
        self.name = name                    # Public
        self.__price = price                # Private
        self.__enrolled_students = 0        # Private
        self.__max_students = max_students  # Private
        self._instructor = None             # Protected
    
    # Getter for price
    def get_price(self):
        return self.__price
    
    # Setter for price (with validation)
    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            print(f"Price updated to ${self.__price}")
        else:
            print("Price must be positive")
    
    # Method to enroll (with validation)
    def enroll_student(self):
        if self.__enrolled_students < self.__max_students:
            self.__enrolled_students += 1
            print(f"Student enrolled! Total: {self.__enrolled_students}")
        else:
            print("Course is full!")
    
    # Getter for enrollment count
    def get_enrollment_count(self):
        return self.__enrolled_students
    
    # Method to check if course is full
    def is_full(self):
        return self.__enrolled_students >= self.__max_students
    
    # Get course info
    def get_info(self):
        status = "FULL" if self.is_full() else "OPEN"
        return f"""
        📚 Course: {self.name}
        💰 Price: ${self.__price}
        👥 Enrolled: {self.__enrolled_students}/{self.__max_students}
        📊 Status: {status}
        """

# Create course
course = Course("Python Programming", 99, 3)

# Public attribute - direct access OK
print(course.name)  # Python Programming

# Private attributes - can't access directly
# print(course.__price)  # AttributeError
# print(course.__enrolled_students)  # AttributeError

# Use methods to access/modify
print(course.get_price())  # 99

course.set_price(149)      # Price updated to $149
course.set_price(-50)      # Price must be positive

# Enroll students with validation
course.enroll_student()    # Student enrolled! Total: 1
course.enroll_student()    # Student enrolled! Total: 2
course.enroll_student()    # Student enrolled! Total: 3
course.enroll_student()    # Course is full!

print(course.get_info())
# 📚 Course: Python Programming
# 💰 Price: $149
# 👥 Enrolled: 3/3
# 📊 Status: FULL