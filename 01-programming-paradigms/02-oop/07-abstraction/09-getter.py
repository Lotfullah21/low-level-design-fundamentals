class Details:
    def __init__(self, name, duration):
        # we did not use _ in name attribute because we want the python to see the same pattern here as well so that it calls the setter method here as well.
        self.name = name
        self.duration = duration
        
    def __str__(self):
        return f"this gives details about {self.name}"
    # by using setter and getter, we do not allow the user to directly access attribute but rather it should go through setters and getters. 
    # in getters and setters we can write our defensive mechanism code, instead of directly writing them in __init__ method.
    @property
    def name(self):
        # using self._attributeName so that there is no colliding with setter.
        return self._name
    
    @name.setter
    def name(self,name):
        # adding defensive condition inside a setter.
        if name.lower() not in ["maths","science","machine learning","deep learning"]:
            raise ValueError("Invalid name")
        self._name = name
        
def main():
    details = get_info()
    print(details.name)


def get_info():
    name = input("Name: ")
    duration = input("Duration: ")
    return Details(name, duration)

if __name__ == "__main__":
    main()
