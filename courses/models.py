from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    preview = models.ImageField(upload_to='courses/preview', blank=True, null=True, verbose_name='Картинка')
    owner = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Владелец')
    update = models.ManyToManyField('users.User', blank=True, null=True, verbose_name='Обновление курса', related_name='courses_update')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
