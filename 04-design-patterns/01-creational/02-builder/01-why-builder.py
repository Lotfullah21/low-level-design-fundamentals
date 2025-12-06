# PROBLEM: Without Builder Pattern

class Course_BAD:
    """Constructor nightmare - too many parameters!"""
    
    def __init__(
        self,
        title: str,
        description: str,
        instructor_id: int,
        price: float,
        currency: str = "USD",
        duration_weeks: int = 4,
        difficulty: str = "Beginner",
        has_certificate: bool = True,
        has_video: bool = True,
        has_quizzes: bool = True,
        has_assignments: bool = False,
        has_forum: bool = True,
        language: str = "English",
        subtitles: list = None,
        prerequisites: list = None,
        tags: list = None,
        thumbnail_url: str = None,
        promo_video_url: str = None,
        is_published: bool = False
    ):
        self.title = title
        self.description = description
        self.instructor_id = instructor_id
        self.price = price
        self.currency = currency
        self.duration_weeks = duration_weeks
        self.difficulty = difficulty
        self.has_certificate = has_certificate
        self.has_video = has_video
        self.has_quizzes = has_quizzes
        self.has_assignments = has_assignments
        self.has_forum = has_forum
        self.language = language
        self.subtitles = subtitles or []
        self.prerequisites = prerequisites or []
        self.tags = tags or []
        self.thumbnail_url = thumbnail_url
        self.promo_video_url = promo_video_url
        self.is_published = is_published


# Usage - NIGHTMARE! 
course = Course_BAD(
    "Python for Beginners",
    "Learn Python from scratch",
    instructor_id=42,
    price=49.99,
    "USD",
    6,
    "Beginner",
    True,
    True,
    True,
    False,
    True,
    "English",
    ["Spanish", "French"],
    ["None"],
    ["python", "programming"],
    "https://...",
    "https://...",
    False,
)
# What does True, True, False mean? No idea! 


