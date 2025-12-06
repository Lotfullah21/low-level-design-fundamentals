## Repository Pattern

Separates data access logic from business logic. Acts as a collection-like interface for accessing domain objects.

The Repository Pattern sits as an abstraction layer between the business logic (views/services) and the data layer (the Django Manager/ORM). It's essentially a dedicated place to store all of our data access logic.

`Simple analogy`: Library - we ask the librarian for a book, we don't go into the storage room, the librarian handles the searching and bringing the book to us.

## When to Use the Repository Pattern

| Use Repository                         | Don't Use Repository             |
| -------------------------------------- | -------------------------------- |
| Abstract database queries              | Simple one-line queries in views |
| Make testing easier (mock repository)  | Prototype / throwaway code       |
| Switch databases without changing code | Single query used only once      |
| Complex queries used multiple times    | Pure Django admin usage          |

**Rule:** If you're writing the same query in **2+ places**, _use a Repository_.

## Usage Frequency in Django

| Context            | Frequency   | Why                                   |
| ------------------ | ----------- | ------------------------------------- |
| Complex operations | Essential   | Enrollment, payment, order processing |
| Views              | Very common | Views call services, not repositories |
| API endpoints      | Very common | Business logic between view & data    |
| Background tasks   | Very common | Celery tasks should use services      |

**Reality:** This is **THE most important pattern** in Django.  
Use it **everywhere**.

## Flowchart

              ┌──────────────────┐
              │      VIEW        │
              │  (No ORM here!)  │
              └──────────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     SERVICE      │
              │ Business logic   │
              │ No DB queries    │
              └──────────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │   REPOSITORY     │
              │ All ORM queries  │
              │ Abstraction layer│
              └──────────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │       ORM        │
              │  Django QuerySet │
              └──────────────────┘
                       │
                       ▼
              ┌──────────────────┐
              │     DATABASE     │
              └──────────────────┘

- **Views** → call **Services**, never the ORM
- **Services** → call **Repositories**, never the ORM
- **Repositories** → contain _all_ database queries
- **ORM** → interacts with PostgreSQL/MySQL/etc.
- **Database** → holds persistent data

flowchart LR

    %% =======================
    %% STYLES
    %% =======================
    classDef badNode fill:#FF453A,stroke:#B81F17,stroke-width:2px,color:#fff;
    classDef goodNode fill:#34C759,stroke:#1D8833,stroke-width:2px,color:#fff;
    classDef neutral fill:#4DA3FF,stroke:#1A73E8,stroke-width:2px,color:#fff;
    classDef warn fill:#FF9F0A,stroke:#C67A00,stroke-width:2px,color:#fff;


    %% =======================
    %% BAD FLOW (LEFT SIDE)
    %% =======================
    subgraph BAD["BAD (Anti-Pattern): ORM inside Views"]
        BView[View]:::badNode
        BQuery[View Calls ORM<br/>Duplicate Queries Everywhere]:::warn
        BORM[ORM]:::badNode
        BDB[(Database)]:::badNode

        BView --> BQuery --> BORM --> BDB
    end


    %% =======================
    %% GOOD FLOW (RIGHT SIDE)
    %% =======================
    subgraph GOOD["GOOD (Repository Pattern)"]
        GView[View]:::neutral
        GService[Service<br/>Business Logic]:::goodNode
        GRepo[Repository<br/>All ORM Queries]:::goodNode
        GORM[ORM]:::goodNode
        GDB[(Database)]:::goodNode

        GView --> GService --> GRepo --> GORM --> GDB
    end

## Without vs With Repository

```py
# views.py - Queries scattered everywhere
def get_active_courses(request):
    courses = Course.objects.filter(is_active=True, is_published=True)
    return Response(CourseSerializer(courses, many=True).data)

def get_instructor_courses(request):
    courses = Course.objects.filter(is_active=True, is_published=True, instructor=request.user)
    return Response(CourseSerializer(courses, many=True).data)

# services.py - Same query repeated
def enroll_student(student, course):
    course = Course.objects.filter(is_active=True, is_published=True).get(id=course.id)
    # Business logic...
```

#### What is .objects?

In Django, every Model class must have at least one Manager. By convention, this is named objects.

Think of the Model class (Course) as a blueprint for a single row of data. Think of objects (the Manager) as the Database Administrator.

objects is the tool that speaks SQL.

This is "Administrator" tool

`The Model (Course) says`: "I define what the data looks like (name, type)."
`The Manager (objects) says`: "I handle the actual SQL. I fetch, save, filter, and create rows."
`Course.objects.filter(...)` works because Course inherits the objects tool from Manager model, and that tool knows how to run the standard .filter() command.

### Problems:

- Repeated query logic
- Hard to test (need real database)
- Change query = update 10+ places
- Business logic mixed with data access

```py
# repositories.py - Single source of truth
class CourseRepository:
    def get_active_courses(self):
        return Course.objects.filter(is_active=True, is_published=True)

    def get_by_id(self, course_id):
        return self.get_active_courses().get(id=course_id)

    def get_by_instructor(self, instructor):
        return self.get_active_courses().filter(instructor=instructor)

# views.py - Clean
def get_active_courses(request):
    repo = CourseRepository()
    courses = repo.get_active_courses()
    return Response(CourseSerializer(courses, many=True).data)

# services.py - Clean
def enroll_student(student, course_id):
    repo = CourseRepository()
    course = repo.get_by_id(course_id)
    # Business logic...
```

### Benefits:

- Query logic in one place
- Easy to test (mock repository)
- Change query once, affects everywhere
- Clear separation of concerns

## Repository Method Naming Convention

| Operation           | Method Name Pattern  | Examples                                     |
| ------------------- | -------------------- | -------------------------------------------- |
| **Get one**         | `get_by_*`           | `get_by_id()`, `get_by_email()`              |
| **Get many**        | `get_*`              | `get_active_courses()`, `get_all()`          |
| **Filter**          | `filter_by_*`        | `filter_by_category()`, `filter_by_status()` |
| **Check existence** | `exists_*` or `is_*` | `exists(id)`, `is_enrolled()`                |
| **Create**          | `create`             | `create(data)`                               |
| **Update**          | `update`             | `update(id, data)`                           |
| **Delete**          | `delete`             | `delete(id)`                                 |
| **Count**           | `count_*`            | `count_active()`, `count_enrolled()`         |

## Testing

1. ### Testing without Repository

```py
# Hard to test - needs real database
def test_enroll_student():
    student = User.objects.create(username='test')
    course = Course.objects.create(title='Test Course')
    # Test logic...
```

2. ### With Repository (Easy to Test)

```python Mock the repository
class MockCourseRepository:
    def get_by_id(self, course_id):
        return Course(id=course_id, title='Mock Course')

# Test without database
def test_enroll_student():
    mock_repo = MockCourseRepository()
    service = EnrollmentService(course_repo=mock_repo)
    # Test logic without touching database
```

## Flow

```text
User Request
    ↓
View (HTTP handling)
    ↓
Service (Business Logic)
    ├── Validation
    ├── Calling repositories
    ├── Orchestrating operations
    ├── Sending emails
    └── Side effects
    ↓
Repository (Data Access)
    ├── Get from DB
    ├── Save to DB
    └── Query DB
    ↓
Database
```

```py
# BAD - Repository doing business logic
class EnrollmentRepository:
    def enroll(self, user, course):
        if not course.is_active:  # Business logic in repository!
            raise ValidationError("Course not active")

        if Enrollment.objects.filter(user=user, course=course).exists():
            raise ValidationError("Already enrolled")  # Business logic!

        return Enrollment.objects.create(user=user, course=course)

# GOOD - Repository just handles data
class EnrollmentRepository:
    def create(self, user, course):
        return Enrollment.objects.create(user=user, course=course)

    def exists(self, user, course):
        return Enrollment.objects.filter(user=user, course=course).exists()

# Business logic in service
class EnrollmentService:
    def enroll(self, user, course):
        if not course.is_active:  # Business logic here!
            raise ValidationError("Course not active")

        if self.repo.exists(user, course):
            raise ValidationError("Already enrolled")

        return self.repo.create(user, course)
```

`Repository` = CRUD operations (dumb data access)
`Service` = Business rules, validation, orchestration (smart logic)
If it's just getting/saving data → Repository
If there are rules, validations, side effects → Service uses Repository

## Template

```py
class YourService:
    def __init__(self, repo1=None, repo2=None):
        self.repo1 = repo1 or Repository1()
        self.repo2 = repo2 or Repository2()

    def do_something(self, data):
        # 1. Get data
        obj = self.repo1.get_by_id(data['id'])

        # 2. Validate (business rules)
        self._validate(obj, data)

        # 3. Execute business logic
        result = self.repo1.update(obj.id, **data)

        # 4. Side effects
        self._send_notification(obj)

        return result

    def _validate(self, obj, data):
        """Private validation method"""
        if not obj.is_active:
            raise ValidationError("Not active")

    def _send_notification(self, obj):
        """Private helper method"""
        # Notification logic
        pass
```

## Django Project Structure

```
apps/
├── users/
│   ├── models.py
│   ├── repositories.py
│   ├── services.py        # ← UserService
│   ├── views.py           # Uses UserService
│   └── tests/
│       ├── test_services.py
│       └── test_repositories.py
├── courses/
│   ├── services.py        # ← CourseService, EnrollmentService
│   └── ...
```

## When to Use Service Layer

| Use Case                             | Use Service Layer | Don't Use Service Layer |
| ------------------------------------ | ----------------- | ----------------------- |
| Complex business logic               | Yes               | No                      |
| Multiple repositories                | Yes               | No                      |
| Validation rules                     | Yes               | No                      |
| Side effects (emails, notifications) | Yes               | No                      |
| Transaction management               | Yes               | No                      |
| Simple CRUD                          | No                | Yes                     |
| Single DB query                      | No                | Yes                     |
| Just displaying data                 | No                | Yes                     |
| Read-only operations                 | No                | Yes                     |
| Admin panel CRUD                     | No                | Yes                     |

### **Rule:**

If there are **business rules** or **multiple steps**, use the **Service Layer**.

## Service vs Repository vs View

## Service vs Repository vs View

| Layer          | Responsibility | Example                        | Dependencies       | Testing                 |
| -------------- | -------------- | ------------------------------ | ------------------ | ----------------------- |
| **View**       | HTTP handling  | Parse request, return response | Calls services     | Integration tests       |
| **Service**    | Business logic | Validation, orchestration      | Calls repositories | Unit tests (mock repos) |
| **Repository** | Data access    | Query database                 | Calls ORM          | Database tests          |

## 🚫 Common Mistakes & Fixes

| Mistake                             | Correct Approach                  |
| ----------------------------------- | --------------------------------- |
| Business logic in views             | Put business logic in services    |
| Services querying database directly | Services should use repositories  |
| Fat services (god classes)          | Small, focused service classes    |
| No dependency injection             | Inject repositories in `__init__` |
| Public helper methods               | Private helpers using `_prefix`   |

Flow: View → Service → Repository → Database
