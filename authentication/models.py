from django.contrib.auth.models import AbstractUser
from django.db import models

from authentication.validators.user import check_birth_date, check_email


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Локация"
        verbose_name_plural = "Локации"

    def __str__(self):
        return self.name


class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = "admin", "Администратор"
        MODERATOR = "moderator", "Модератор"
        MEMBER = "member", "Пользователь"

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.MEMBER)
    age = models.PositiveSmallIntegerField(null=True)
    location = models.ManyToManyField(Location)
    birth_date = models.DateField(null=True, validators=[check_birth_date])
    email = models.EmailField(unique=True, validators=[check_email])

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = ["username"]

    def __str__(self):
        return self.username
