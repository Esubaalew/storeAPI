from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.management import call_command


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'