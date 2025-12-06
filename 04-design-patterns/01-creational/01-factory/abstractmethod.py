from abc import ABC, abstractmethod

class Course(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

class Python(Course):
    def get_name(self):
        return "Hello python"
    
class MachineLearning(Course):
    pass

py = Python()
# ml = MachineLearning() # Error: "Course.get_name" is not implemented
print(py.get_name())