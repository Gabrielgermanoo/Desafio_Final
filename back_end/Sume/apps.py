from django.apps import AppConfig


class SumeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Sume'

    def ready(self) -> None:
        from Sume import signals