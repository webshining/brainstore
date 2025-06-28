from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User

    readonly_fields = ("telegram_username", "language_code", "first_name", "last_name")
    list_display = ("username", "telegram_username", "is_staff", "is_active")
    search_fields = ("username", "telegram_username")
    ordering = ("username",)

    fieldsets = (
        ("Admin", {"fields": ("username", "is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Telegram Info", {"fields": ("telegram_id", "first_name", "last_name", "telegram_username", "language_code")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", "is_active", "is_superuser", "is_staff"),
            },
        ),
    )
