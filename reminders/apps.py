from django.apps import AppConfig


class ReminderConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "reminders"

    def ready(self):
        from reminders import receivers  # noqa
