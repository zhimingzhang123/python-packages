# __init__.py
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app


__all__ = ['celery_app']



# app1_tasks.py
from __future__ import absolute_import, unicode_literals
from celery import task


@task()
def task_number_one():
    # Do something...
 app2_tasks.py
from __future__ import absolute_import, unicode_literals
from celery import task


@task()
def task_number_two():
    # Do another thing...
    # 


# celery.py
from __future__ import absolute_import, unicode_literals
import os

from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')

# Using a string here means the worker don't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


# settings.py
from celery.schedules import crontab

# Celery application definition
# http://docs.celeryproject.org/en/v4.0.2/userguide/configuration.html

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Makassar'
CELERY_BEAT_SCHEDULE = {
    'task-number-one': {
        'task': 'app1.tasks.task_number_one',
        'schedule': crontab(minute=59, hour=23)
    },
    'task-number-two': {
        'task': 'app2.tasks.task_number_two',
        'schedule': crontab(minute=0, hour='*/3,10-19')
    }
}