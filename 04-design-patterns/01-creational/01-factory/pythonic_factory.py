from abc import ABC, abstractmethod

# Step 1: Abstract base class
class Content(ABC):
    @abstractmethod
    def render(self) -> str| None:
        pass
    @abstractmethod
    def validate(self) -> bool| None:
        pass

# Step 2: Create concrete class
class VideoContent(Content):
    def __init__(self, title, url):
        self.title:str = title
        self.url:str = url
    
    def render(self):
        return f"<video>{self.url}</video>"

    def validate(self):
        return self.url.endswith((".mp4", ".mov"))
    

class QuizContent(Content):
    def __init__(self, title, questions):
        self.title = title
        self.questions = questions
    
    def render(self):
        return f"<h1>{self.title}</h1>"
    
    def validate(self) -> bool | None:
        return super().validate()
    
# Step 3: Create factory class
class ContentFactory:
    @staticmethod
    def create(content_type, **kwargs):
        types = {
            "quiz":QuizContent,
            "video":VideoContent,
        }
        object = types.get(content_type)
        if not object:
            raise ValueError(f"Unknown content type: {content_type}")
        return object(**kwargs)
    
video = ContentFactory.create("video",title = "Intro to functions",url="https://youtu.be/8TRijfkvUfQ?si=BX_RwN_LaLpW2DM4")
quiz = ContentFactory.create("quiz",title="Python basics",questions="https://youtu.be/8TRijfkvUfQ?si=BX_RwN_LaLpW2DM4")

print(video.validate())
print(video.render())