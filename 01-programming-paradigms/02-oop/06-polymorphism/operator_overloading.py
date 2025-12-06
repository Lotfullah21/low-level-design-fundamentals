class Course:
    def __init__(self, name,prerequisite, duration):
        self.name = name
        self.prerequisite = prerequisite
        self.duration = duration
        
    
    def __str__(self):
        return f"{self.name} requires {self.prerequisite} as its prerequisite and it takes {self.duration} months to complete. "
    
    # self refers whatever object on the left and other refers to the object on the right side of + operator.
    def __add__(self, other):
        duration = self.duration + other.duration
        prerequisites = self.prerequisite + " and " + other.prerequisite
        name = self.name + " and " + other.name
        # after object on the left and object on the right together, return one new object with the resulted operations.
        return Course(name,prerequisites,duration)
        
machineLearning = Course("Machine learning","Statistics",6)
deepLearning = Course("Deep learning","Calculus",3)

new_course = machineLearning + deepLearning 
print(new_course)