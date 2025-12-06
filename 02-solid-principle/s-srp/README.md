## S - Single Responsibility Principle (SRP)

Definition: A class should have ONE and ONLY ONE reason to change, meaning it should have only ONE job.

If it has more than one axis of change, it will become harder to maintain.

Don't put the functions that changes for different reasons in the same class.
Don't make concerns in the same class.

##### The Core Idea

If you can describe what a class does with `"AND"`, it's doing too much:

- "This class manages users AND sends emails AND generates reports"
- "This class manages user data"

##### Why SRP Matters

- `Easier to Understand`: Small, focused classes are easier to comprehend
- `Easier to Test`: Test one thing at a time
- `Easier to Modify`: Changes in one area don't affect others
- `Easier to Debug`: Bugs are isolated to specific responsibilities
- `Better Reusability`: Single-purpose classes can be reused elsewhere

### Example 1: User Management System

#### BAD: Violating SRP

```py
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def save_to_database(self):
        """Saving user to database"""
        import sqlite3
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (self.name, self.email, self.password)
        )
        conn.commit()
        conn.close()
        print(f"User {self.name} saved to database")

    def hash_password(self):
        """Hashing password"""
        import hashlib
        self.password = hashlib.sha256(self.password.encode()).hexdigest()
        print(f"Password hashed for {self.name}")

    def generate_report(self):
        """Generating user report"""
        report = f"""
        USER REPORT
        ===========
        Name: {self.name}
        Email: {self.email}
        Account Status: Active
        """
        with open(f"{self.name}_report.txt", "w") as f:
            f.write(report)
        print(f"Report generated for {self.name}")
```

#### Problems:

- 3 Different Responsibilities: User data, database, reporting

- 4 Reasons to Change:

  - Change user attributes → modify class
  - Change database (PostgreSQL) → modify class
  - Change validation rules → modify class
  - Change report format (PDF) → modify class

- Hard to Test: Need actual database,file system
- Tight Coupling: User class knows about, SQLite, file I/O

#### GOOD: Following SRP

```py
# 1. User class - ONLY manages user data
class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def get_info(self):
        return {
            'name': self.name,
            'email': self.email
        }


# 2. UserRepository - ONLY handles database operations
class UserRepository:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def save(self, user: User):
        """Save user to database"""
        cursor = self.db_connection.cursor()
        cursor.execute(
            "INSERT INTO users VALUES (?, ?, ?)",
            (user.name, user.email, user.password)
        )
        self.db_connection.commit()
        print(f"User {user.name} saved to database")

    def find_by_email(self, email):
        """Find user by email"""
        cursor = self.db_connection.cursor()
        cursor.execute("SELECT * FROM users WHERE email = ?", (email,))
        return cursor.fetchone()

# 5. PasswordHasher - ONLY handles password hashing
class PasswordHasher:
    @staticmethod
    def hash(password):
        """Hash password using SHA256"""
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def verify(password, hashed_password):
        """Verify password against hash"""
        return PasswordHasher.hash(password) == hashed_password


# 6. UserReportGenerator - ONLY generates reports
class UserReportGenerator:
    def generate_text_report(self, user: User):
        """Generate text report for user"""
        report = f"""
        USER REPORT
        ===========
        Name: {user.name}
        Email: {user.email}
        Account Status: Active
        """
        with open(f"{user.name}_report.txt", "w") as f:
            f.write(report)
        print(f"Report generated for {user.name}")
        return report

    def generate_pdf_report(self, user: User):
        """Generate PDF report for user"""
        # PDF generation logic
        pass


# Usage Example - Orchestrating all the single-responsibility classes
def create_new_user(name, email, password, db_connection, smtp_config):

    # hash password
    hashed_password = PasswordHasher.hash(password)

    # create user
    user = User(name, email, hashed_password)

    # save to database
    repo = UserRepository(db_connection)
    repo.save(user)

    # generate report
    report_gen = UserReportGenerator()
    report_gen.generate_text_report(user)

    return user


# Testing is now easy
def test_email_validator():
    assert EmailValidator.is_valid("test@example.com") == True
    assert EmailValidator.is_valid("invalid-email") == False
    print("Email validation tests passed")

def test_password_hasher():
    hashed = PasswordHasher.hash("mypassword")
    assert PasswordHasher.verify("mypassword", hashed) == True
    assert PasswordHasher.verify("wrongpassword", hashed) == False
    print("Password hashing tests passed")

test_email_validator()
test_password_hasher()
```

### How to Identify SRP Violations

- Class name contains "AND": UserAndEmailManager
- Too many methods: Class with 15+ methods
- Multiple imports: Imports database, email, file I/O, HTTP libraries
- Long class: 500+ lines in one class
- Hard to name: Can't describe class purpose in one sentence
- Many reasons to change: Different teams need to modify it

#### Questions to Ask:

- "What does this class do?" If answer has "and", it violates SRP
- "Why would this class change?" If more than one reason, it violates SRP
- "Can I describe this class in one sentence?" If no, it violates SRP

#### Rule of Thumb

###### A method should:

- Do ONE thing
- Be 5-15 lines (max 30 lines)
- Have ONE level of abstraction
- Be easily testable
- Have a clear, descriptive name
