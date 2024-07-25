from django.core.management import BaseCommand

from users.models import Payment


class Command(BaseCommand):
    def handle(self, *args, **options):
        payment_list = [
            {'user': 'hatan2235@mail.ru', 'date': '07/23/2006 14:30',
             'amount': 6500,
             'course': 'Разработка'},
            {'name': 'Python', 'description': 'Обучение наиболее популярному языку разработки',
             'video': 'http://127.0.0.1:8000/',
             'course': 'Разработка', 'lesson': 'Django', 'method': 'перевод на счет'}
        ]
        for payment in payment_list:
            Payment.objects.create(**payment)
