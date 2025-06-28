from .models import User


async def create_or_update_user(
    id: int,
    username: str,
    first_name: str,
    last_name: str,
    language_code: str,
) -> User:
    user, created = await User.objects.aupdate_or_create(
        telegram_id=id,
        defaults={
            "telegram_username": username,
            "first_name": first_name,
            "last_name": last_name,
        },
    )
    if created and user.language_code != language_code:
        user.language_code = language_code
        await user.asave(update_fields=["language_code"])

    return user
