def add_timestamp(cls):
    """
    This decorator takes a class object (cls) as input.
    It returns a modified class object.
    """
    # 1. Define a new method to be added to the class
    def timestamp(self):
        import time
        return time.strftime("%Y-%m-%d %H:%M:%S")
    
    # 2. Add the new method to the class dynamically
    cls.timestamp = timestamp
    
    # 3. Return the modified class
    return cls

@add_timestamp
class Event:
    def __init__(self, name):
        self.name = name

# Usage:
event = Event("Meeting")
# The class decorator dynamically added the timestamp method!
print(event.timestamp()) 