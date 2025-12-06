class Calculator:
    TOTAL = 100
    def __init__(self, name):
        self.name= name
        
    # instance method
    def mul(self):
        print(self.name)
    # static method
    @staticmethod
    def add(a, b):
        print(a + b)

    # class method
    @classmethod    
    def subtract(cls):
        print(cls.TOTAL - 1)
    
calc = Calculator("Scientific")
calc.add(12,10)
calc.subtract()