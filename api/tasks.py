from celery import shared_task
from django.core.mail import send_mail
from .models import Subscriber

@shared_task
def notify_subscribers_new_subject(subject_name):
    emails = Subscriber.objects.values_list('email', flat=True)
    if not emails:
        return

    subject = f"Новый предмет: {subject_name}"
    message = f"Был добавлен новый предмет: {subject_name}. Проверьте сайт для подробностей."

    send_mail(
        subject=subject,
        message=message,
        from_email="shyngysuly04@gmail.com",
        recipient_list=list(emails),
        fail_silently=False,
    )
