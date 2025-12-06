## Package

A package is a directory that Python treats as a module group, allowing us to organize code into sub-modules.

If you want Python to treat your folders as importable modules, each folder must contain an `__init__.py` file.

Here’s the clear rule:

A folder becomes a Python package only when it contains `__init__.py`

Folder structure with `__init__.py` (WORKS)

```py
architectural_pattern/
    __init__.py
    repository/
        __init__.py
        user_repo.py
    service/
        __init__.py
        user_service.py
```

```py
from architectural_pattern.repository.user_repo import UserRepository
from architectural_pattern.service.user_service import UserService
```

#### Why is it required?

`__init__.py` tells Python:

- “This folder is a package. You can import from it.”

It also lets us:

- group code logically
- avoid name conflicts
- control what gets imported
- structure large apps
- separate logic (service, repository, models, utils)
- avoid naming conflicts
- make clean imports
