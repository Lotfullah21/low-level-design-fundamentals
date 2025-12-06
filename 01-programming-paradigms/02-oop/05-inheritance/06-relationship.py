class Course:
    def __init__(self, name):
        self.name = name
        
class ProgrammingCourse(Course):
    def __init__(self, name, language):
        super().__init__(name)
        self.language = language

    def get_info(self):
        return f"{self.language} is from a {self.name} course"

class Framework(ProgrammingCourse):
    def __init__(self, name, language, framework):
        super().__init__(name, language)
        self.framework = framework

    def get_info(self):
        return f"{self.framework} framework is from {self.language} language"
    
programming = Course("Programming")
python = ProgrammingCourse("Programming","Python")
framework = Framework("Programming","Python","Django")
print(isinstance(programming, Course))
print(isinstance(python, Course))
print(isinstance(framework, Course))
print(isinstance(programming, Framework))