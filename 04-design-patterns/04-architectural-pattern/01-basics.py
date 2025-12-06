from dataclasses import dataclass, field

class UserNative:
    def __init__(self, id:int, name:str="Anonymous", tags:list[str] = []):
        self.id = id
        self.name=name
        self.tags = tags
# Usage
user1 = UserNative(12)
print(user1.name,user1.id, user1.tags)



# With dataclass, the __init__ method is avoided
@dataclass
class User:
    id:int
    # for mutable objects, default factory should be used
    # new list per instance
    tags:list[str]=field(default_factory=list)
    name:str = "Anonymous"

user_d = User(120)
print(user_d)

