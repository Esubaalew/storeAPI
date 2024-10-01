from django.apps import AppConfig


class APIConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'API'

    def ready(self) -> None:
        import API.signals