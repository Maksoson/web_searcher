from django.apps import AppConfig


class MainPageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.main_page'

    def ready(self):
        import applications.main_page.signals
