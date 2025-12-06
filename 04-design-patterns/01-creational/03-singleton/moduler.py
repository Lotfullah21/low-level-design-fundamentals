# config.py
class _AppConfig:
    def __init__(self):
        self.database_url = "postgresql://localhost/mydb"
        self.redis_url = "redis://localhost:8069"
        self.debug = True
    
    def get(self, key):
        # getattr() returns the value of an attribute from an object.
        return getattr(self, key, None) # getattr(object, "attribute_name", default_value)

# Create single instance at module level
app_config = _AppConfig()
