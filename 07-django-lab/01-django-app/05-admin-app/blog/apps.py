from django.apps import AppConfig


class BlogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
    # this will be shown in the admin name section for blog model
    verbose_name = 'blog management'