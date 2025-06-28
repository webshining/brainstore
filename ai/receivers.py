from django.dispatch import receiver

from ai.tasks import process_request
from bot.signals import process_request_signal


@receiver(process_request_signal)
def _process_request(message: str, user_id: int, *args, **kwargs):
    process_request.delay(message, user_id)
