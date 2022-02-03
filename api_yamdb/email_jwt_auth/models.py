from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class UserEmailCode(models.Model):
    username = models.CharField(max_length=64, unique=False)
    email = models.EmailField()
    confirmation_code = models.IntegerField()
