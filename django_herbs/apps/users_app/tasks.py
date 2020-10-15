from django.core.mail import send_mail
from django_herbs.celery import app

@app.task
def send_asyncio():

    # setting smtp
    subject = "NAME"
    FROM = 'from@example.com'
    TO = 'to@example.com'
    message_link = "LINK"


    num_letter = send_mail(
        'Hello, {}'.format(subject),
        'Follow the link for registration: {}'.format(message_link),
        FROM,
        [TO],
        fail_silently=False,
    )

