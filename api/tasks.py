from celery import shared_task
from django.core.mail import send_mail

def generate_flag_message(content):
    return f"Your comment was flagged for moderation: '{content[:50]}...'"

@shared_task
def send_flag_notification(email, content):
    send_mail(
        subject="Comment Flagged",
        message=generate_flag_message(content),
        from_email="no-reply@moderation.com",
        recipient_list=[email],
        fail_silently=True,
    )