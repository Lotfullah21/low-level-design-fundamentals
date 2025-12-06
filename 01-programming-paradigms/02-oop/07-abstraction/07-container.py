class Courses:
    def __init__(self):
        self.chapters = []

    def add(self, chapter):
        return self.chapters.append(chapter)
    
    # makes it indexable
    def __getitem__(self, index):
        return self.chapters[index]
    
    # Makes 'len' work
    def __len__(self):
        return len(self.chapters)
    
    # Makes 'in' work
    def __contains__(self, chapter):
        return chapter in self.chapters



courses = Courses()
courses.add("Python")
courses.add("Web Dev")
print(courses.chapters)
print(courses[0])
print(len(courses))
print("Python" in courses)