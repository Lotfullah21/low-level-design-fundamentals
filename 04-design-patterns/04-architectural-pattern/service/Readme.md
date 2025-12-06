## Service Layer

The Service Layer is a high-level organizing principle for the entire application structure. Its main goal is to decouple the business logic from the presentation (e.g., Django Views) and the data access (e.g., Repositories/Managers).

Service Layer:

- coordinates multiple repositories.
- handles complex calculations or validation rules.
- manages transactions that span several data operations.

Essentially, the Service Layer is the "service" our application provides, while the Repository is just responsible for data management.

# Architectural Relationship

The **Service Layer acts as a firewall** between web framework (Django/DRF) and core data logic.

| Layer                   | Responsibility                                            | Pattern Implemented        |
| ----------------------- | --------------------------------------------------------- | -------------------------- |
| **Presentation / View** | Handles HTTP Request/Response, calls the Service.         | None                       |
| **Service Layer**       | Business logic, transactions, coordination.               | **Service Pattern**        |
| **Repository Layer**    | Aggregates and abstracts data queries (find, save, list). | **Repository Pattern**     |
| **Manager / ORM**       | Handles instance creation logic (acts like a Factory).    | **Factory Method Pattern** |
| **Model**               | The data structure definition (the Product).              | None                       |

# Architecture: Service → Repository → Manager → Model

## ASCII diagram (plain text)

```
Presentation / View
       |
       v
  +-----------------+
  |  Service Layer  |  <- business logic, transactions, orchestration
  +-----------------+
       |
       v
  +---------------------+
  | Repository Layer    |  <- find, list, save, complex queries
  +---------------------+
       |
       v
  +--------------------+
  | Manager / ORM      |  <- instance creation, low-level DB/ORM glue
  +--------------------+
       |
       v
  +----------------+
  | Model (Product) |  <- data structure / schema
  +----------------+
```

---

## Full folder structure (Django example)

```
project_root/
├─ manage.py
├─ requirements.txt
├─ config/                 # Django project settings + wsgi/asgi
│  ├─ settings.py
│  └─ urls.py
├─ apps/
│  ├─ users/
│  │  ├─ __init__.py
│  │  ├─ models.py                # Django models
│  │  ├─ managers.py              # custom model managers / factory-like creation
│  │  ├─ repositories/            # data access layer for User and related entities
│  │  │  ├─ __init__.py
│  │  │  ├─ user_repository.py
│  │  │  └─ token_repository.py
│  │  ├─ services/                # business logic and orchestration
│  │  │  ├─ __init__.py
│  │  │  ├─ user_service.py
│  │  │  └─ auth_service.py
│  │  ├─ api/                     # DRF views / serializers / urls
│  │  │  ├─ views.py
│  │  │  ├─ serializers.py
│  │  │  └─ urls.py
│  │  ├─ tests/
│  │  │  ├─ test_repositories.py
│  │  │  └─ test_services.py
│  │  └─ apps.py
│  ├─ courses/
│  │  ├─ models.py
│  │  ├─ repositories/
│  │  ├─ services/
│  │  └─ api/
│  └─ ...
├─ common/
│  ├─ exceptions.py
│  ├─ types.py
│  └─ db.py
└─ docs/
   └─ architecture.md
```

### Notes on structure

- `repositories/` are small, focused modules whose responsibilities are: **querying**, **persisting**, and **mapping** between database/ORM and domain objects
- `services/` are where **transactions**, **cross-repository orchestration**, and **business rules** live. Keep them thin and testable.
- `managers.py` (custom managers) are the natural place to put factory-like creation (`MyModel.objects.create_xxx(...)`) and ORM-specific helpers.
- `common/db.py` holds transaction helpers and session management so services can open/commit/rollback transactions without talking to Django settings directly.

---

## Example: `user_repository.py`

```python
# apps/users/repositories/user_repository.py
from typing import Optional
from apps.users.models import User

class UserRepository:
    """Small wrapper around Django ORM for users. Keep ORM code here so services remain DB-agnostic."""

    def get_by_id(self, pk: int) -> Optional[User]:
        return User.objects.filter(id=pk).first()

    def get_by_email(self, email: str) -> Optional[User]:
        return User.objects.filter(email__iexact=email).first()

    def create(self, **attrs) -> User:
        return User.objects.create(**attrs)

    def update(self, user: User, **attrs) -> User:
        for k, v in attrs.items():
            setattr(user, k, v)
        user.save()
        return user

    def exists(self, **filters) -> bool:
        return User.objects.filter(**filters).exists()
```

---

## Example: `user_service.py`

```python
# apps/users/services/user_service.py
from common.db import atomic
from apps.users.repositories.user_repository import UserRepository

class UserService:
    def __init__(self, user_repo: UserRepository | None = None):
        self.user_repo = user_repo or UserRepository()

    def register_user(self, email: str, password: str, **extra) -> dict:
        # Example orchestration — validate, create events, send mail
        if self.user_repo.exists(email__iexact=email):
            raise ValueError("email already exists")

        with atomic():
            user = self.user_repo.create(email=email, password=password, **extra)
            # maybe create profile, tokens, emit event
        return {"id": user.id, "ema d il": user.email}

    def change_email(self, user_id: int, new_email: str) -> dict:
        user = self.user_repo.get_by_id(user_id)
        if not user:
            raise LookupError("user not found")
        if self.user_repo.exists(email__iexact=new_email):
            raise ValueError("email already in use")
        with atomic():
            self.user_repo.update(user, email=new_email)
        return {"id": user.id, "email": new_email}
```
