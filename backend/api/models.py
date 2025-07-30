"""Database models for the API application."""

from django.db import models


class Task(models.Model):
    """Модель Task."""

    title = models.CharField(verbose_name='Заголовок', max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
