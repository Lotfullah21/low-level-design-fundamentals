class Course:
    def __init__(self,topics):
        self.topics = topics
    
    @classmethod
    def python(cls):
        return cls(['functions','modules','objects'])

    @classmethod
    def machine_learning(cls):
        return cls(['supervise learning']) 
    

machine_learning = Course.machine_learning()
python = Course.python()
print(python.topics)
print(machine_learning.topics)