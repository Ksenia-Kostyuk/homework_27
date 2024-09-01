from django.db import models

from courses.models import Course


class Lesson(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/preview', blank=True, null=True, verbose_name='Картинка')
    video = models.URLField(max_length=200, verbose_name='Ссылка на видеоурок')
    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL, verbose_name='Курс', related_name='lessons')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
