class Calculator:
    TOTAL = 0
    def __init__(self, name):
        self.name= name

    # to access class attribute
    def add(self):
        print(self.name)
        # using classname.attribute_name
        print(Calculator.TOTAL)
        # or __class__ method
        print(self.__class__.TOTAL)
    
calc = Calculator("Scientific")
calc.add()
