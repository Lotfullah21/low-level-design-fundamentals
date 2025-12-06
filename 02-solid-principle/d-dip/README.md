## D - Dependency Inversion Principle (DIP)

`Definition`: High-level modules should not depend on low-level modules. Both should depend on abstractions.
Ideally, no two concrete classes should depend on each other, their dependence should be via interface.

#### In simple terms:

- Don't depend on concrete classes
- Depend on interfaces/abstractions instead
- "Program to an interface, not an implementation"

`High-Level Module`: The "Boss" (Business Logic, Strategy).
`Low-Level Module`: The "Worker" (Database, API, Email Sender, File System).

DIP Rule: The Boss shouldn't know the details of the Worker. The Boss should just hold a contract (Interface), and we plug in whatever Worker fits that contract.

### The Analogy: The Wall Socket

`High Level`: Your Laptop (It needs power).
`Low Level`: The Nuclear Power Plant (It provides power).
`Abstraction (The Middleman)`: The Wall Socket.

Laptop doesn't know if the electricity comes from a nuclear plant, a solar panel, or a hamster running on a wheel. It just cares about the Socket (Interface). This allows us to change the power source without soldering wires directly into the laptop.

The Dependency Inversion Principle (DIP) is specifically about the relationship between Business Logic (High-Level) and Tools (Low-Level).

#### Why DIP Matters

- `Flexibility`: Easy to swap implementations
- `Testability`: Mock dependencies easily
- `Decoupling`: Changes in one module don't break others
- `Maintainability`: Clear separation of concerns

### Notification Manager

```py
class EmailService:
    def send_mail(self, message):
        print(f"Sending Email -------> {message}")

class SMSService:
    def send_sms(self, message="SMS Notification"):
        print(f"Sending SMS -------> {message}")

class NotificationManager:
    def __init__(self):
        self.service = EmailService()
        self.sms_service = SMSService()

    def send_notification(self, message):
        self.service.send_mail(message)

    def send_sms(self, message):
        self.sms_service.send_sms(message)

notification_manger = NotificationManager()
notification_manger.send_notification("Hello, I am from email service")
notification_manger.send_sms("Hello, I am from email service")
```

#### Why is this bad?

- `Hard to change`: If we want to change from Email to SMS, we have to go into NotificationManager and change the business logic just to add a tool.
- `Hard to test`: We can't test the Manager without actually sending emails.

### DIP Pattern: Dependency Injection

The key to DIP: Inject dependencies from outside!

```py
# Bad: Creating dependencies inside
class Service:
    def __init__(self):
        self.db = MySQLDatabase()  # Created inside!

# Good: Inject dependencies
class Service:
    def __init__(self, db: Database):  # Injected from outside!
        self.db = db
```

### How to Identify DIP Violations

#### Red Flags:

- self.dependency = ConcreteClass() in constructor
- Can't easily swap implementations
- Hard to test (need real database, real API, etc.)
- High-level classes import low-level classes directly
