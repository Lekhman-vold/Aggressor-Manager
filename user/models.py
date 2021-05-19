from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_status = models.BooleanField(default=False)
    bio = models.CharField(max_length=1000, blank=True)
    location = models.CharField(max_length=200, blank=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    # phone_number = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return f'Username: {self.user}, Work status: {self.work_status}'
