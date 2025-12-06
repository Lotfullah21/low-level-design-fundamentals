
from django.db import models

class User(models.Model): 
    user_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=90)
    password = models.CharField(max_length=30)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)