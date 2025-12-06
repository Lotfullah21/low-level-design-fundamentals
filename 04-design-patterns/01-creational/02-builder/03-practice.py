class Course:
    def __init__(self):
        # Basic info
        self.title: str =""
        self.description:str = ""
        
        # Pricing
        self.price: float = 0.0
        
        # Content
        self.duration_in_weeks: int = 4
        self.language: str = "Dari"

        # Features
        self.has_video: bool = True
        self.has_quiz: bool = False

    
    def __repr__(self) -> str:
        return f"{self.title} will be finished in {self.duration_in_weeks} and it's language is {self.language}"

class CourseBuilder:
    def __init__(self):
        self._course = Course()
    def _set_title(self, title):
        self._course.title=title
        # ← Returns the builder object itself
        return self
    def _set_price(self, price):
        self._course.price = price
         # ← Returns the builder object itself
        return self
    def _set_language(self, language):
        self._course.language = language
         # ← Returns the builder object itself
        return self
    
    def build(self):
        if not self._course.title:
            raise ValueError("The course should have a title")
        if not self._course.duration_in_weeks:
            raise ValueError("The course should have duration")
        if not self._course.language:
            raise ValueError("The course should have language")
        return self._course
    

course = CourseBuilder()._set_language("English")._set_price(120)._set_title("Machine learning").build()
print(course)


# Chaining = Skipping the intermediate variable:

# Instead of this:
builder = CourseBuilder()
builder._set_title("Python")
builder._set_price(49.99)
course = builder.build()

# Do this (same thing):
course = CourseBuilder()._set_title("Python")._set_price(49.99).build()

# Without return self:
def set_title(self, title):
    self._course.title = title
    # Returns None by default

builder._set_title("Python")._set_price(49.99)  #  Error!
# Can't call .set_price() on None



# With return self:
def set_title(self, title):
    self._course.title = title
    return self  # Returns builder

builder._set_title("Python")._set_price(49.99)  # Works!
# Each method returns the builder, so you can keep calling methods