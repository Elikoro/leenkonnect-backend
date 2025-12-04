from django.apps import AppConfig


class NotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'notifications'
    
    def ready(self):
        # Import and connect signal handlers. Import inside ready() to avoid
        # circular imports during Django startup and migrations.
        from . import signals  # noqa: F401
