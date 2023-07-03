import os
from celery import Celery


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chollosite.settings')
app = Celery('chollosite')
app.config_from_object('django.conf.settings', namespace='CELERY')
app.autodiscover_tasks()


# docker pull rabbitmq
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management

# celery -A myshop worker -l info .....instead of this
# celery -A chollosite worker --loglevel=info ....use this


# At some point the cart doesnt show the actual number of items
