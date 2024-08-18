from datetime import timedelta, datetime

from celery import shared_task
from users.models import User


@shared_task
def user_chek_filter_last_login():
    users = User.objects.all()

    for user in users:
        time_difference = datetime.now() - user.last_login
        if time_difference > timedelta(days=30):
            user.is_active = False



