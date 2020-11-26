from django.core.mail import send_mail
from django_herbs.celery import app


@app.task
def send_asyncio(subject, from_email, to_email, link,):

    # setting smtp
    subject = subject
    FROM = from_email
    TO = to_email
    message_link = link

    num_letter = send_mail(
        'Hello, {}'.format(subject),
        'Follow the link for registration: {}'.format(message_link),
        FROM,
        [TO],
        fail_silently=False,
    )


