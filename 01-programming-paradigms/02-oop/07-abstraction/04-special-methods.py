class Python:
    def __init__(self, name, chapters) -> None:
        self.name = name
        self.chapters = chapters
        
    def get_name(self):
        return f"{self.name}"
    
    def get_chapters(self):
        return f"{self.chapters}"
    
    # this dunder method is usually for users
    def __str__(self) -> str:
        return f"{self.name} has {self.chapters} chapters"
    # this method is for developers
    def __repr__(self) -> str:
        return str(self.chapters)
    # def __len__(self):
    #     return self.chapters


python = Python("Django", 12)
print(python)
print(repr(python))
print(len(python))
