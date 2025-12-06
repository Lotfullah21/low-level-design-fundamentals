from abc import ABC, abstractmethod
class Course(ABC):

    @abstractmethod
    def get_name(self) ->str:
        """Every course must implement this"""
        pass

    @abstractmethod
    def get_chapters(self) ->str:
        """Every Course must implement this"""
        pass
    

class Python(Course):
    def __init__(self, name, chapters) -> None:
        self._name = name
        self._chapters = chapters
    
    def get_name(self):
        return f"{self._name}"
    
    def get_chapters(self):
        return f"{self._chapters}"

python = Python("Django", 12)
print(python.get_chapters())
print(python.get_name())