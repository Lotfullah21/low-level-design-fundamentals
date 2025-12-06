from django.db.models import Count
from user_model import User

    
# all queries in repository
class UserRepository:

    def create(self, **data):
        return User.objects.create(**data)
    
    def delete(self, user_id):
        user = User.objects.filter(id=user_id).first()
        if user:
            user.delete()
            return True
        return False
    
    def update(self, user_id, data):
        User.objects.filter(id=user_id).update(**data)
        return self.get_by_id(user_id)
    
    def get_by_id(self, user_id):
        return User.objects.filter(id=user_id)
 
    def get_by_user_name(self, user_name):
        return User.objects.filter(user_name=user_name)
    
    def get_by_email(self, email):
        return User.objects.filter(email=email)
    
    def count_users(self):
        return User.objects.count()

# services.py
user_repo = UserRepository()
create = user_repo.create(name="ali", email="ali@gamil.com")
user = user_repo.get_by_id(user_id=1)