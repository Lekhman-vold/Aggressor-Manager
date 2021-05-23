from django.db import models
from django.contrib.auth.models import User


class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField(blank=True)
    status = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(auto_now=False, blank=True)

    def __str__(self):
        return f"Tasks {self.title}, status: {self.status} worked user: {self.user}"
