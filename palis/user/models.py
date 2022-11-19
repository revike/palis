from decimal import Decimal

from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    """Таблица пользователей"""
    telegram_id = models.PositiveBigIntegerField(
        unique=True, null=True, verbose_name='id telegram')

    def __str__(self):
        return self.username

    class Meta:
        db_table = "user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Profile(models.Model):
    """Таблица профиля пользователя"""
    CHOICES = (
        ('h', 'почасовая оплата'),
        ('p', 'сдельная оплата')
    )
    user_id = models.OneToOneField(User, on_delete=models.CASCADE,
                                   verbose_name='user_id')
    phone_number_regex = RegexValidator(regex=r"^\+?1?\d{8,15}$")
    phone = models.CharField(validators=[phone_number_regex], max_length=16,
                             unique=True, verbose_name='phone')
    departament = models.CharField(max_length=128, verbose_name='departament')
    post = models.CharField(max_length=128, verbose_name='post')
    salary = models.DecimalField(max_digits=8, decimal_places=2, default=0,
                                 validators=[
                                     MinValueValidator(Decimal('0.00'))],
                                 verbose_name='salary')
    payment_type = models.CharField(max_length=1, choices=CHOICES,
                                    verbose_name='payment_type')
    created = models.DateTimeField(auto_now_add=True, verbose_name='created')
    updated = models.DateTimeField(auto_now=True, verbose_name='update')

    def __str__(self):
        return self.user_id

    class Meta:
        db_table = "profile"
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
