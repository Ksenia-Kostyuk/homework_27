from django.core.management import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        courses_list = [
            {'name': 'Тестирвоание', 'description': 'Подготовка к профессии тестировщика'},
            {'name': 'Разработка', 'description': 'Подготовка к профессии разработчика'}
        ]
        for course in courses_list:
            Course.objects.create(**course)
