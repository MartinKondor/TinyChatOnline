from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

from .interfaces import JsonInterface


class User(models.Model, JsonInterface):
    email = models.EmailField(max_length=200)
    password_hash = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)
    last_login = models.DateTimeField(default=timezone.now, null=True)

    @staticmethod
    def make_password(password, *args, **kwargs) -> str:
        return make_password(password, *args, **kwargs)

    @staticmethod
    def check_password(*args, **kwargs) -> bool:
        return check_password(*args, **kwargs)

    def __str__(self):
        return self.email


class Message(models.Model, JsonInterface):
    text = models.TextField()
    from_user_id = models.IntegerField()  # Foreign key
    to_user_id = models.IntegerField()  # Foreign key
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text
