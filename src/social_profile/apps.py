from django.apps import AppConfig


class SocialProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'social_profile'

    def ready(self):
        print("Importing social profile signals")
        import social_profile.signals
