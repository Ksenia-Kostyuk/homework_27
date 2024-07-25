from django.core.management import BaseCommand

from lessons.models import Lesson


class Command(BaseCommand):
    def handle(self, *args, **options):
        lessons_list = [
            {'name': 'Django', 'description': 'Основы самого удобного веб-фреймворка',
             'video': 'http://127.0.0.1:8000/',
             'course': 'Разработка'},
            {'name': 'Python', 'description': 'Обучение наиболее популярному языку разработки',
             'video': 'http://127.0.0.1:8000/',
             'course': 'Разработка'}
        ]
        for lesson in lessons_list:
            Lesson.objects.create(**lesson)
