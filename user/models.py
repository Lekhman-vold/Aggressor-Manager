from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
