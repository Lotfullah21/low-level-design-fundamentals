from repository.user_repo import UserRepository
from errors import validationError
from django.contrib.auth.hashers import make_password



class UserService:
    def __init__(self, user_repo=None):
        self.user_repo:UserRepository = user_repo or UserRepository()

    def register_user(self, user_name, email, password):

        self._validate_registration(email, user_name)
        hashed_password = self._hash_password(password)

        user = self.user_repo.create(user_name=user_name,
                                    email=email, 
                                    password=hashed_password)
        self._create_default_profile(user)
        
        return user
    
    def _validate_registration(self, email, user_name):
        if self.user_repo.get_by_email(email):
            raise ValueError("User with this email already registered")
        if self.user_repo.get_by_user_name(user_name):
            raise ValueError("User with this username already registered")

    def _hash_password(self, password):
        return make_password(password)
    
    def _create_default_profile(self, user):
        pass

# Testing the Service with a fake dependency
mock_repo = UserRepository()
test_service = UserService(user_repo=mock_repo)



    


