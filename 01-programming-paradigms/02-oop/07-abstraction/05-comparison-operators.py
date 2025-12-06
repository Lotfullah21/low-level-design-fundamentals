class Student:
    def __init__(self, age, name):
        self.age = age
        self.name = name
    # __eq__ represents ==
    def __eq__(self, other: object) -> bool:
        return self.age == other.age
    # __gt__ represents >
    def __gt__(self, other: object):
        return self.age > other.age
    # __lt__ represents <
    def __lt__(self, other:object):
        return self.age > other.age
    

ali = Student(12, "ali")
ahmad = Student(14, "ahmad")
print(ali>ahmad)
print(ali==ahmad)