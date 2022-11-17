from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Таблица пользователей"""
    telegram_id = models.PositiveBigIntegerField(
        unique=True, null=True, verbose_name='id telegram')

    def __str__(self):
        return self.username

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
