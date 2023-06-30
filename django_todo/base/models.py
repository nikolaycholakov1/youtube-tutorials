from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = (
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High'),
    )
    TITLE_MAX_LEN = 200
    PRIORITY_MAX_LEN = 6

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    complete = models.BooleanField(
        default=False,
    )

    created = models.DateTimeField(
        auto_now_add=True,
    )

    priority = models.CharField(
        null=False,
        blank=False,
        choices=PRIORITY_CHOICES,
        max_length=PRIORITY_MAX_LEN,
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']
