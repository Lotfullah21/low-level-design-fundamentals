class CourseEnrollment:
    def __init__(self, age, grade):
        self._age = age
        self._grade = grade
    
    def _check_age(self):
        return self._age>=12
    
    def _check_grade(self):
        return self._grade>=6
    
    def _find_course(self):
        print("Registering...")

    def _enroll(self):
        print("Enrolling...")
    
    def enrolled(self):
        if self._check_age() and self._check_grade():
            ali._find_course()
            ali._enroll()
            print("Enrollment Done!!!")
        else:
            print("Enrollment Failed")
    
age = int(input("Enter age: "))
grade = int(input("Enter grade: "))

ali = CourseEnrollment(age, grade)
ali.enrolled()