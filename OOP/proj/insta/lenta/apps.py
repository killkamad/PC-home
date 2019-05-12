from django.apps import AppConfig


class LentaConfig(AppConfig):
    name = 'lenta'

    def ready(self):
        import lenta.signals