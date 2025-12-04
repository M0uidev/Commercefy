from django.apps import AppConfig


class AppCommercefyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appCommercefy'

    def ready(self):
        import appCommercefy.signals
