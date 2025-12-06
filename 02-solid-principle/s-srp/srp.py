# Bad
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

# class User:
#     def __init__(self, name, email, password):
#         self.name = name
#         self.email = email
#         self.password = password

#     def get_info(self):
#         return {
#             'name': self.name,
#             'email': self.email
#         }
    