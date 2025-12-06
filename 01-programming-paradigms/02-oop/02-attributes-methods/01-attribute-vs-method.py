class Course:
    # class attributes
    enrolled_students = 0
    platform=""

    def __init__(self, name:str, rating:int):
        self.name = name
        self.rating = rating
    
    def get_name(self) ->str:
        return self.name
    
    def enroll_student(self, n)->int:
        # modify the class attribute using object_name.class_instance
        Course.enrolled_students = Course.enrolled_students + n
        return Course.enrolled_students
    
    def change_platform(self,new_platform) ->str:
       Course.platform = new_platform
       return Course.platform

ml = Course("ML",2)
ml.enroll_student(1)
ml.enroll_student(1)
ml.enroll_student(11)
print(ml.get_name())
print(ml.enrolled_students)
# changes for all instances of courses
ml.change_platform("Hooshmandlab")
print(ml.platform)
# modifies only for a specific instance
ml.platform="Youtube"
print(ml.platform)
python = Course("Python",12)
print(python.platform)
# modifies for all instances
Course.platform="Coursera"
print(python.platform)
print(ml.platform)


