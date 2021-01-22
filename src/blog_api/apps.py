from django.apps import AppConfig


class BlogApiConfig(AppConfig):
    name = 'blog_api'

    def ready(self):
        import blog_api.signals
