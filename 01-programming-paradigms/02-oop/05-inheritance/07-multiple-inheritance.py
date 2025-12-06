class Course:
    def __init__(self, name):
        self.name = name
        
class ProgrammingCourse:
    def __init__(self, language):
        self.language = language

    def get_info(self):
        return f"{self.language}"

class Framework(ProgrammingCourse, Course):
    def __init__(self, name,framework, language):
        ProgrammingCourse.__init__(self,language)
        Course.__init__(self, name)
        self.framework = framework

    def get_info(self):
        return f"{self.framework} framework is from {self.language} language"
    
python = ProgrammingCourse("Python")
python.language
django = Framework("Programming", "django","python")
print(django.language)
print(django.name)
