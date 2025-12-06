### Interface Segregation Principle (ISP)

`Definition`: Clients should not be forced to depend on interfaces they do not use. It's better to have many specific interfaces than one general-purpose interface.

The motto of ISP is: `"Don't force a class to sign a contract it can't fulfill."`

If we create a massive interface with 20 methods, every class that implements it must write code for all 20 methods, even if it only needs 2 of them.

#### In simple terms:

- Don't create fat interfaces with too many methods
- Split large interfaces into smaller, specific ones
- Classes should only implement methods they actually need

The key idea: Many small, focused interfaces are better than one large, bloated interface.

Unlike languages like Java or C#, Python does not have a specific interface keyword. Instead, Python uses Abstract Base Classes (ABCs) to create interfaces.

To create an interface in Python, We need to:

- Import `ABC` and `abstractmethod` from the abc module.
- Define methods without any code (`pass`) and mark them with `@abstractmethod`.

### Why ISP Matters

1. Prevents Unnecessary Dependencies

- Classes don't depend on methods they don't use
- Reduces coupling
- Easier to understand what a class actually needs

2. Cleaner Code

- No empty method implementations
- No "not implemented" exceptions
- Clear responsibilities

3. Better Flexibility

- Easy to implement only what we need
- Mix and match interfaces
- Add new implementations without breaking existing code

4. Easier Maintenance

- Changes to unused methods don't affect us
- Smaller, focused interfaces are easier to understand
- Less risk of breaking changes

##### Violating ISP:

A OldPrinter is forced to implement scan even though it can't do it.

```py
from abc import ABC, abstractmethod

class Machine(ABC):
    @abstractmethod
    def print_doc(self, doc): pass

    @abstractmethod
    def scan_doc(self, doc): pass

class OldPrinter(Machine):
    def print_doc(self, doc):
        print("Printing...")

    def scan_doc(self, doc):
        # Forced to implement this, violates ISP
        raise NotImplementedError("Old printers can't scan!")
```

##### Following ISP:

Instead of one giant interface, we break it down into capabilities based on behavior.

Split the interface into smaller, specific parts.

```py
class Printer(ABC):
    @abstractmethod
    def print_doc(self, doc):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self, doc):
        pass

class OldPrinter(Printer):
    def print_doc(self, doc):
        print("Printing...")

class ModernPrinter(Printer, Scanner):
    def print_doc(self, doc):
        print("Printing...")

    def scan_doc(self, doc):
        print("Scanning...")
```

### ISP in Real World

### 1. Cloud Storage APIs

```py
# Segregated interfaces
Readable → read()
Writable → write()
Deletable → delete()
Versionable → list_versions(), restore_version()


class S3Bucket(Readable, Writable, Deletable, Versionable):
    pass

class PublicCDN(Readable):
    pass
```

### 2. User Permissions

```py
class ViewPermission:
    def can_view(self): pass

class EditPermission:
    def can_edit(self): pass

class DeletePermission:
    def can_delete(self): pass

class AdminUser(ViewPermission, EditPermission, DeletePermission):
    pass

class Viewer(ViewPermission):
    pass
```

#### Initialization order for multiple inheritance

```py
class Car(Movable, FuelVehicle):
    pass
```

Only, the first one gets initialized and the second one do not get `initialized` at all.

###### The MRO

`Car → Movable → FuelVehicle → ABC → object`
