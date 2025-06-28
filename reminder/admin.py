from django.contrib import admin

from .models import Reminder


@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    model = Reminder

    list_display = ("title", "cron", "datetime")
