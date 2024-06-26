from django.db import models

from api.core.models import BaseModel


class Event(BaseModel):
    LIMITATIONS = (
        ("Everyone", "everyone"),
        ("School", "school"),
        ("Student", "student"),
        ("Professional", "professional"),
    )

    title = models.CharField(
        max_length=255,
    )

    users = models.ManyToManyField(
        "users.User",
        related_name="events",
        blank=True,
    )

    start_date = models.DateField(
        null=True,
        blank=True,
    )

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        default="",
    )

    is_online = models.BooleanField(
        default=True,
    )

    location = models.CharField(
        max_length=512,
        default="",
    )

    limitation = models.CharField(
        max_length=64,
        choices=LIMITATIONS,
        default="everyone",
    )

    tree = models.JSONField()

    def __str__(self):
        return self.title

    def run_algorythm(self):
        pass
