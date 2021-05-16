from django.db import models
from django.contrib.auth.models import User


class UserModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    work_status = models.BooleanField(default=False)
    user_description = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f'Username: {self.user}, Work status: {self.work_status}'
