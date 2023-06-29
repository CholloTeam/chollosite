import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chollosite.settings')
app = Celery('chollosite')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()


# celery -A myshop worker -l info .....instead of this
# celery -A project worker --loglevel=info ....use this
