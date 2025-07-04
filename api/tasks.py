from celery import shared_task
from django.core.mail import send_mail

def generate_flag_message(content, content_type):
    return f"Your {content_type} was flagged for moderation: '{content[:50]}...'"

@shared_task
def send_flag_notification(email, content, content_type):
    send_mail(
        subject=f"{content_type.capitalize()} Flagged",
        message=generate_flag_message(content, content_type),
        from_email="no-reply@moderation.com",
        recipient_list=[email],
        fail_silently=True,
    )