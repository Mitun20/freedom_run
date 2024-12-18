from django.apps import AppConfig

class FreedomrunConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'freedomrun'

    def ready(self):
        import freedomrun.signals  
