# Step 1: Create the base class
from abc import ABC, abstractmethod
class Course(ABC):
    @abstractmethod
    def name(self)-> None| str:
        pass
    @abstractmethod
    def save(self) -> None | str:
        pass

# Step 2: Concrete products
class Python(Course):
    def name(self):
        return "Python"
    def save(self):
        return "Saving python course..."

class Java(Course):
    def name(self):
        return "Java"

    def save(self):
        return "Saving java course..."
    
    
## Step 3: Add factory method (creator)
class CourseFactory(ABC):
    @abstractmethod
    def create_course(self) -> Course:
        pass

    def new_course(self):
        course = self.create_course()
        print(course.name())
        print(course.save())
        return course

## Step 4: Concrete creates that uses factory method
class PythonCourse(CourseFactory):
    def create_course(self):
        return Python()

class JavaCourse(CourseFactory):
    def create_course(self) -> Course:
        return Java()
    
## Step 5: USAGE
python = PythonCourse()
python.new_course()
java = JavaCourse()
java.new_course()
