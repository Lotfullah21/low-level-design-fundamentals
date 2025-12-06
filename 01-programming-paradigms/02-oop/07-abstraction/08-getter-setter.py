class Courses:
    def __init__(self, name, price):
        self.name = name
        self._price = price

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price2(self, val):
        if val<0:
            raise ValueError("Price cannot be negative")
        self._price = val


python = Courses("Python", 10)
print(python.name)
# obj.setter, should exactly match what we wrote on setter method.
python.price2 = -120
print(python._price)