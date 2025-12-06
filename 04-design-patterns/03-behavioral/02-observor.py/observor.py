# apps.py or signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from user_model import User


