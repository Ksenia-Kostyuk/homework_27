from config.settings import EMAIL_HOST_USER
from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_information_about_update_course(email):
    """Отправляет сообщение о выходе обновления"""
    send_mail('Обновление курса', 'Вышли новые материалы курса', EMAIL_HOST_USER, [email])
