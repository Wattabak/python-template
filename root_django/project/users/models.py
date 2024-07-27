import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models

from .managers import UserManager


class User(AbstractUser):
    uuid = models.UUIDField(default=uuid.uuid4, )
    objects = UserManager()

    def __str__(self):
        return str(self.uuid)
