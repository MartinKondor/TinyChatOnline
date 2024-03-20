import json

from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class JsonInterface:
    """
    Make the models.Model able to be converted to JSON
    """

    def to_dict(self):
        obj = {}
        class_fields = self.__class__._meta.get_fields()
        fields = [f.name for f in class_fields]

        for field in fields:
            if not hasattr(self, field):
                continue
            obj[field] = str(getattr(self, field))

        return obj

    def to_json(self, indent=4):
        return json.dumps(self.to_dict(), indent=indent)


class User(models.Model, JsonInterface):
    email = models.EmailField(max_length=200)
    password_hash = models.CharField(max_length=200, null=True)
    created_date = models.DateTimeField(default=timezone.now, null=True)

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
