from django.apps import AppConfig


class StudentapiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'studentapi'


    # def ready(self):
    #     from . import signals