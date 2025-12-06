## 1. Repository Pattern

It is an architectural pattern from domain driver design (DDD).
It is a layer that acts as middle man between the business logic and data storage.

Think of it like a librarian:

- You ask: "Give me the book about Python"
- You DON'T care if it's in:
  - Shelf A, row 3
  - The basement
  - Another library branch
  - Digital archive

The librarian handles WHERE and HOW. You just get your book.

```ssh
WITHOUT Repository:
┌─────────────────┐
│ UserService     │
│ (Business Logic)│──► Directly writes SQL queries
│                 │──► Knows about database tables
│                 │──► Mixed concerns
└─────────────────┘

WITH Repository:
┌─────────────────┐
│ UserService     │──► "Get me user with ID 5"
│ (Business Logic)│    (Doesn't know HOW)
└────────┬────────┘
         │
┌────────▼────────┐
│ UserRepository  │──► Handles SQL, caching, etc.
│ (Data Access)   │
└─────────────────┘
```

1. Real HLAB Scenarios

| Scenario / Feature           | Without Repository                                                    | With Repository                                     |
| ---------------------------- | --------------------------------------------------------------------- | --------------------------------------------------- |
| Get enrolled courses         | `SELECT * FROM enrollments WHERE user_id=?` scattered across ~5 files | `enrollment_repo.get_by_user(user_id)` in one place |
| Switch from MySQL to MongoDB | Change raw SQL in 50+ places 😱                                       | Change 1 repository class                           |
| Test user registration       | Requires a real database running                                      | Use `InMemoryUserRepository` for fast unit tests    |

## WHY Repository Pattern? (The Deep Reasons)?

### 1. Separation of Concerns

Business Logic: "I need user enrollments"
Repository: "Here they are" (you don't care if it's from SQL, Redis, API)

### 2. Testing

````py
# Without Repository: Need real database running
def test_enrollment():
    service = CourseService_BAD("real_database.db")  # Slow, fragile
    service.enroll_student(1, 101)

# With Repository: Instant tests
def test_enrollment():
    repo = InMemoryEnrollmentRepository()  # Fast, no setup
    service = EnrollmentService_GOOD(repo)
    service.enroll_student(1, 101)```
````

### 3. Future-Proofing

Startup grows:

Year 1: SQLite
Year 2: PostgreSQL (need more power)
Year 3: Mix of Postgres + Redis cache

Without Repository: Rewrite 100+ files
With Repository: Create PostgresEnrollmentRepository, done

### 4. Multiple Data Sources

```py
class HybridEnrollmentRepository(IEnrollmentRepository):
    def __init__(self, db_repo, cache_repo):
        self.db = db_repo      # PostgreSQL
        self.cache = cache_repo  # Redis

    def get_by_user(self, user_id: int):
        # Check cache first
        cached = self.cache.get(f"user:{user_id}:enrollments")
        if cached:
            return cached

        # Fallback to database
        data = self.db.get_by_user(user_id)
        self.cache.set(f"user:{user_id}:enrollments", data)
        return data
```

Your service code? Doesn't change.

| Component                 | Repository                                 | Real-World Benefit                                                                  |
| ------------------------- | ------------------------------------------ | ----------------------------------------------------------------------------------- |
| **User Authentication**   | `UserRepository`                           | Easily switch from a local database to OAuth or Firebase Auth                       |
| **Video Streaming**       | `VideoRepository`                          | Swap from AWS S3 to Cloudflare Stream with zero service changes                     |
| **Certificates**          | `CertificateRepository`                    | Archive or move data to cold storage without touching app logic                     |
| **Analytics**             | `AnalyticsRepository`                      | Experiment with different time-series DBs (e.g., InfluxDB, ClickHouse) effortlessly |
| **Courses & Enrollments** | `CourseRepository`, `EnrollmentRepository` | Change schema or database (SQL ↔ NoSQL) without affecting business logic            |
| **Payments**              | `PaymentRepository`                        | Integrate new gateways (Stripe, PayPal, Flutterwave) with minimal code changes      |
| **Notifications**         | `NotificationRepository`                   | Swap between Twilio, SendGrid, or Firebase Cloud Messaging easily                   |

### 5. dataclass

It kills the boiler plate code and create an instance.

```py
from dataclass
```

## bound parameters

We write SQL with holes (placeholders), and we pass the values separately. The driver binds each value into its hole safely, treating it as data, not SQL code

```py
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE enrollments(id INTEGER PRIMARY KEY, course_id TEXT)")

# ❌ BAD: string building (vulnerable + fragile)
user_input = "101); DROP TABLE enrollments; --"
bad_sql = f"INSERT INTO enrollments(course_id) VALUES ({user_input})"
# Running this would try to execute multiple statements (dangerous) — don't do this.

# ✅ GOOD: bound params (placeholders + separate values)
good_sql = "INSERT INTO enrollments(course_id) VALUES (?)"
conn.execute(good_sql, (user_input,))  # driver binds the *literal string* safely
conn.commit()

# Prove it: table still exists and the "dangerous" text was stored as DATA, not code
row = conn.execute("SELECT course_id FROM enrollments").fetchone()
print("Stored value:", row[0])
# → Stored value: 101); DROP TABLE enrollments; --   (just text, no table dropped)

```

## What happened step-by-step

- SQL with placeholders: "INSERT ... VALUES (?)"
- Values separately: (user_input,)
- Driver binds: it quotes/escapes/types the value correctly.
- DB sees data, not code: the scary text goes into the column; it doesn’t run.

### Why this matters

- Security: stops SQL injection (no accidental code execution).
- Correct typing: None → NULL, ints as ints, bytes as BLOBs, etc.
- Less quoting pain: you never add quotes yourself; the driver does it.

If the idea to remember is just one sentence: placeholders in SQL + values passed separately = the driver binds them safely as data.

## Driver

driver is the Python library that talks to The database. It implements the DB-API 2.0 spec and acts as the adapter between The code and the DB engine: it opens connections, executes SQL, binds parameters, converts Python types ↔ SQL types, manages transactions, and raises standardized exceptions.

### Quick mental model

`The code → driver (adapter) → database.`

### Example drivers:

- SQLite: sqlite3 (built-in; file-based, no server)
- PostgreSQL: psycopg / psycopg2
- MySQL/MariaDB: mysql-connector-python, PyMySQL
- SQL Server: pyodbc

What the driver does (at a glance)

- Connection/Cursor: connect(), cursor()
- Execute SQL: cursor.execute(sql, params) (uses the driver’s placeholder style)
- Parameter binding: safely injects values into SQL (prevents SQL injection)
- Type conversion: None→NULL, int→INTEGER, datetime→TEXT/TIMESTAMP, etc.
- Transactions: commit(), rollback()
- Errors: consistent exceptions (e.g., sqlite3.IntegrityError, DatabaseError)

## Driver vs ORM

**Driver**: low-level, you write SQL strings yourself.

**ORM** (e.g., SQLAlchemy ORM, Django ORM): higher-level; generates SQL and still uses a driver under the hood to actually talk to the DB.

when we say “the driver binds parameters,” we mean this library (e.g., sqlite3, psycopg) safely attaches the Python values to the SQL placeholders before sending the statement to the database.
