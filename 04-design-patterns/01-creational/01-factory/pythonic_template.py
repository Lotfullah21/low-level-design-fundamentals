from abc import ABC, abstractmethod

# Step 1: Base class
class YourBase(ABC):
    @abstractmethod
    def method1(self):
        pass

# Step 2: Concrete classes
class Type1(YourBase):
    def __init__(self, **kwargs):
        # Initialize attributes
        pass
    
    def method1(self):
        # Implementation
        pass

class Type2(YourBase):
    def __init__(self, **kwargs):
        pass
    
    def method1(self):
        pass

# Step 3: Factory
class YourFactory:
    @staticmethod
    def create(type_name, **kwargs):
        types = {
            'type1': Type1,
            'type2': Type2
        }
        
        object = types.get(type_name)
        if not object:
            raise ValueError(f"Unknown type: {type_name}")
        
        return object(**kwargs)

# Step 4: Use it
obj = YourFactory.create('type1', param1='value1')