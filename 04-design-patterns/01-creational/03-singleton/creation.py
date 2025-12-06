class DatabaseConnection:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance  = super().__new__(cls)
            cls._instance.connection = "Connected to PostgreSQL"
        return cls._instance
    
db1 = DatabaseConnection()
db2 = DatabaseConnection()


print(db1 is db2)