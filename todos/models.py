from django.db import models


THEME = (
    ('Python', 'Python'),
    ('Django', 'Django'),
    ('Flask', 'Flask'),
    ('FastAPI', 'FastAPI'),
    ('Algorithms', 'Algorithms'),
    ('Other', 'Other')
)


class Todo(models.Model):
    title = models.CharField(max_length=250, blank=True)
    theme = models.CharField(choices=THEME, max_length=20, blank=True)
    description = models.CharField(max_length=1000, blank=True)
    url = models.URLField(max_length=500)
