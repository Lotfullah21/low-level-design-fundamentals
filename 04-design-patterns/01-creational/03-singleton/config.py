import os
class AppConfig:
    # class variable
    _instance = None

    def __new__(cls):
        # instance variables
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.load_config()
        return cls._instance
    
    def load_config(self):
        self.DATABASE_URL = os.getenv("DATABASE_URL","http:localhost/8069")
        self.GCP_KEY = os.getenv("GCP_KEY","#$3FDS23")
        self.REDIS_URL = os.getenv("REDIS_URL", "$2AD3DFE01")

app_config = AppConfig()
print(app_config.DATABASE_URL)