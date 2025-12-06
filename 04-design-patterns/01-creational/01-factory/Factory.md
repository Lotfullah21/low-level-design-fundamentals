from abc import ABC, abstractmethod

# Step 1: Create the interface

class Course(ABC):
@abstractmethod # All courses must have teach method
def teach(self)->str:
pass

# Step 2: Create concrete products

class Python(Course):
def teach(self) -> str:
return "Teaching python"

class Java(Course):
def teach(self) -> str:
return "Teaching Java"

## Step 3: Create the creator with factory methods

class TeachingMode(ABC):
@abstractmethod # This is the FACTORY METHOD
def create_course(self) -> Course:
"""This will be override by the subclasses and decides what teaching mode to be there"""
pass

    def teaching_course(self) ->str:
        course = self.create_course()
        return course.teach()

# Step 4: Concrete creators that implement factory method

class PythonCourse(TeachingMode):
def create_course(self) -> Course:
return Python()

class JavaCourse(TeachingMode):
def create_course(self) -> Course:
return Java()

# Step 5: Usage

create_java = JavaCourse()
create_py = PythonCourse()
print(create_java.teaching_course())
print(create_py.teaching_course())```sh

```

```
