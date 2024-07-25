from django.contrib.auth.models import AbstractUser
from django.db import models

from courses.models import Course
from lessons.models import Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='Почта')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name='Телефон')
    city = models.CharField(max_length=150, blank=True, null=True, verbose_name='Город')
    avatar = models.ImageField(upload_to='users/avatar', blank=True, null=True, verbose_name='Аватар')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    METHOD_CHOICES = [('cash', 'наличные'), ('transfer_to_an_account', 'перевод на счет')]
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, verbose_name='Пользователь')
    date = models.DateTimeField(verbose_name='Дата оплаты')
    amount = models.IntegerField(verbose_name='Сумма оплаты')
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lesson, null=True, on_delete=models.SET_NULL, verbose_name='Оплаченный урок')
    method = models.CharField(max_length=100, choices=METHOD_CHOICES, verbose_name='Способ оплаты')

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
