class CourseEnrollment:
    def __init__(self, age, grade):
        self.age = age
        self.grade = grade
    
    def check_age(self):
        return self.age>=12
    
    def check_grade(self):
        return self.grade>=6
    
    def find_course(self):
        print("Registering...")

    def enroll(self):
        print("Enrolling...")
    
age = int(input("Enter age: "))
grade = int(input("Enter grade: "))

ali = CourseEnrollment(age, grade)
if ali.check_age() and ali.check_grade():
    ali.find_course()
    ali.enroll()
    print("Enrollment Done!!!")