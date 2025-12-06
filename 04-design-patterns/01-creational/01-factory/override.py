class Course():
    def get_course_quality(self) -> str:
        pass

class Python(Course):
    def get_course_quality(self) -> str:
        return "Cool"
    
class MachineLearning(Course):
    def get_course_quality(self) -> str:
        return "Not bad"

print(Course().get_course_quality())
print(MachineLearning().get_course_quality())
print(Python().get_course_quality())
