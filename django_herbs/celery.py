
from __future__ import absolute_import, unicode_literals


import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_herbs.settings')

app = Celery('django_herbs')

app.config_from_object('django.conf:settings', namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)






# Celery настройка

CELERY_ALWAYS_EAGER = True
'''Параметр CELERY_ALWAYS_EAGER позволяет выполнять задачи локально на синхронной основе, а не отправлять их в очередь.'''