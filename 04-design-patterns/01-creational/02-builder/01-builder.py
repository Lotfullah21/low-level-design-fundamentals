# SOLUTION: Builder Pattern

from typing import List, Optional


class Course:
    """Simple, clean data class"""
    
    def __init__(self):
        # Basic info
        self.title: str = ""
        self.description: str = ""
        self.instructor_id: int = 0
        
        # Pricing
        self.price: float = 0.0
        self.currency: str = "USD"
        
        # Content
        self.duration_weeks: int = 4
        self.difficulty: str = "Beginner"
        self.language: str = "English"
        
        # Features
        self.has_certificate: bool = False
        self.has_video: bool = False
        self.has_quizzes: bool = False
        self.has_assignments: bool = False
        self.has_forum: bool = False
        
        # Optional
        self.subtitles: List[str] = []
        self.prerequisites: List[str] = []
        self.tags: List[str] = []
        self.thumbnail_url: Optional[str] = None
        self.promo_video_url: Optional[str] = None
        self.is_published: bool = False
    
    def __repr__(self):
        return f"Course(title='{self.title}', price={self.price}, difficulty='{self.difficulty}')"


class CourseBuilder:
    """Builds Course objects step-by-step"""
    
    def __init__(self):
        self._course = Course()
    
    # Basic info methods
    def set_title(self, title: str):
        self._course.title = title
        return self  # ← Return self for chaining!
    
    def set_description(self, description: str):
        self._course.description = description
        return self
    
    def set_instructor(self, instructor_id: int):
        self._course.instructor_id = instructor_id
        return self
    
    # Pricing methods
    def set_price(self, price: float, currency: str = "USD"):
        self._course.price = price
        self._course.currency = currency
        return self
    
    # Content methods
    def set_duration(self, weeks: int):
        self._course.duration_weeks = weeks
        return self
    
    def set_difficulty(self, level: str):
        """Options: Beginner, Intermediate, Advanced"""
        self._course.difficulty = level
        return self
    
    def set_language(self, language: str):
        self._course.language = language
        return self
    
    # Feature toggles
    def with_certificate(self):
        self._course.has_certificate = True
        return self
    
    def with_video(self):
        self._course.has_video = True
        return self
    
    def with_quizzes(self):
        self._course.has_quizzes = True
        return self
    
    def with_assignments(self):
        self._course.has_assignments = True
        return self
    
    def with_forum(self):
        self._course.has_forum = True
        return self
    
    # Optional content
    def add_subtitle(self, language: str):
        self._course.subtitles.append(language)
        return self
    
    def add_prerequisite(self, prerequisite: str):
        self._course.prerequisites.append(prerequisite)
        return self
    
    def add_tag(self, tag: str):
        self._course.tags.append(tag)
        return self
    
    def set_thumbnail(self, url: str):
        self._course.thumbnail_url = url
        return self
    
    def set_promo_video(self, url: str):
        self._course.promo_video_url = url
        return self
    
    def publish(self):
        self._course.is_published = True
        return self
    
    # Final build method
    def build(self) -> Course:
        """Returns the constructed course"""
        # Validation before building
        if not self._course.title:
            raise ValueError("Course title is required!")
        if not self._course.instructor_id:
            raise ValueError("Instructor ID is required!")
        
        return self._course


# 🎯 USAGE: Beautiful and Readable!

def demo_basic_usage():
    print("=" * 70)
    print("EXAMPLE 1: Basic Course")
    print("=" * 70)
    
    # Build a simple course
    course = (CourseBuilder()
        .set_title("Python for Beginners")
        .set_description("Learn Python from scratch")
        .set_instructor(42)
        .set_price(49.99)
        .set_duration(6)
        .with_video()
        .with_quizzes()
        .with_certificate()
        .build()
    )
    
    print(f"Created: {course}")
    print(f"   Has video: {course.has_video}")
    print(f"   Has certificate: {course.has_certificate}")


def demo_advanced_course():
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Advanced Course with All Features")
    print("=" * 70)
    
    course = (CourseBuilder()
        .set_title("Machine Learning Specialization")
        .set_description("Master ML from theory to practice")
        .set_instructor(123)
        .set_price(299.99, "USD")
        .set_duration(12)
        .set_difficulty("Advanced")
        .set_language("English")
        .add_subtitle("Spanish")
        .add_subtitle("French")
        .add_subtitle("Chinese")
        .add_prerequisite("Python Programming")
        .add_prerequisite("Linear Algebra")
        .add_prerequisite("Statistics")
        .add_tag("machine-learning")
        .add_tag("ai")
        .add_tag("data-science")
        .with_video()
        .with_quizzes()
        .with_assignments()
        .with_forum()
        .with_certificate()
        .set_thumbnail("https://example.com/ml-thumb.jpg")
        .set_promo_video("https://example.com/ml-promo.mp4")
        .publish()
        .build()
    )
    
    print(f"Created: {course}")
    print(f"   Subtitles: {course.subtitles}")
    print(f"   Prerequisites: {course.prerequisites}")
    print(f"   Published: {course.is_published}")


# 🎓 DIRECTOR: Pre-configured builders

class CourseDirector:
    """Pre-defined course templates - convenience layer"""
    
    @staticmethod
    def create_beginner_course(title: str, instructor_id: int) -> Course:
        """Standard beginner course template"""
        return (CourseBuilder()
            .set_title(title)
            .set_instructor(instructor_id)
            .set_price(29.99)
            .set_duration(4)
            .set_difficulty("Beginner")
            .with_video()
            .with_quizzes()
            .with_certificate()
            .build()
        )
    
    @staticmethod
    def create_premium_course(title: str, instructor_id: int) -> Course:
        """Premium course with all features"""
        return (CourseBuilder()
            .set_title(title)
            .set_instructor(instructor_id)
            .set_price(199.99)
            .set_duration(8)
            .set_difficulty("Intermediate")
            .with_video()
            .with_quizzes()
            .with_assignments()
            .with_forum()
            .with_certificate()
            .add_subtitle("Spanish")
            .add_subtitle("French")
            .publish()
            .build()
        )
    
    @staticmethod
    def create_free_course(title: str, instructor_id: int) -> Course:
        """Free course with basic features"""
        return (CourseBuilder()
            .set_title(title)
            .set_instructor(instructor_id)
            .set_price(0.0)
            .set_duration(2)
            .with_video()
            .build()
        )


def demo_director():
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Using Director (Pre-configured Templates)")
    print("=" * 70)
    
    beginner = CourseDirector.create_beginner_course(
        "Intro to Programming", 
        instructor_id=1
    )
    print(f"Beginner course: {beginner}")
    
    premium = CourseDirector.create_premium_course(
        "Full Stack Development",
        instructor_id=2
    )
    print(f"Premium course: {premium}")
    
    free = CourseDirector.create_free_course(
        "Git Basics",
        instructor_id=3
    )
    print(f"Free course: {free}")


# 🔥 REAL WORLD: Query Builder Example

class QueryBuilder:
    """Build SQL queries step-by-step"""
    
    def __init__(self):
        self._table = ""
        self._columns = ["*"]
        self._where_clauses = []
        self._order_by = []
        self._limit = None
    
    def select(self, *columns):
        self._columns = list(columns)
        return self
    
    def from_table(self, table: str):
        self._table = table
        return self
    
    def where(self, condition: str):
        self._where_clauses.append(condition)
        return self
    
    def order_by(self, column: str, direction: str = "ASC"):
        self._order_by.append(f"{column} {direction}")
        return self
    
    def limit(self, count: int):
        self._limit = count
        return self
    
    def build(self) -> str:
        if not self._table:
            raise ValueError("Table name required!")
        
        query = f"SELECT {', '.join(self._columns)} FROM {self._table}"
        
        if self._where_clauses:
            query += f" WHERE {' AND '.join(self._where_clauses)}"
        
        if self._order_by:
            query += f" ORDER BY {', '.join(self._order_by)}"
        
        if self._limit:
            query += f" LIMIT {self._limit}"
        
        return query + ";"


def demo_query_builder():
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Query Builder")
    print("=" * 70)
    
    query = (QueryBuilder()
        .select("id", "title", "price")
        .from_table("courses")
        .where("price > 0")
        .where("is_published = true")
        .order_by("price", "DESC")
        .limit(10)
        .build()
    )
    
    print(f"Generated SQL:\n{query}")


# RUN ALL DEMOS

if __name__ == "__main__":
    demo_basic_usage()
    demo_advanced_course()
    demo_director()
    demo_query_builder()
    
    print("\n" + "=" * 70)
    print("KEY BENEFITS OF BUILDER PATTERN:")
    print("=" * 70)
    print("1. Readable: Chain methods like sentences")
    print("2. Flexible: Build only what you need")
    print("3. Validation: Check before building")
    print("4. Immutable: Build once, don't change")
    print("5. Testable: Easy to create test objects")
    print("=" * 70)