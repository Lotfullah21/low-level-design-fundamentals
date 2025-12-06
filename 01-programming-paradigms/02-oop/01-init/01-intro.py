class Course:
    def __init__(self, name, subjects):
        self.name = name
        self.subjects = subjects

    def get_subjects(self):
        # self refers to the current course object, if self is not here, the program does not know which subjects we are referring to
        return self.subjects

course1 = Course("ML", 12)
print(course1.get_subjects())